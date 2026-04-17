# Vasconcelos API - Public Domain Setup

Setup notes for exposing the Django API publicly under **`api.vasconcelosagricola.com.br`** via Nginx + Let's Encrypt on this VPS (`147.79.81.43`).

## Context

The API runs as a gunicorn process bound to `127.0.0.1:9000`. Nginx terminates TLS on `:443` and reverse-proxies to gunicorn. Certificates are issued and renewed by Let's Encrypt / certbot.

## Prerequisites

- DNS `A` record on the domain registrar (Vercel):
  `api.vasconcelosagricola.com.br → 147.79.81.43`
- Redis, gunicorn venv, and all prerequisites from [setup.md](./setup.md) already in place.

## Steps performed

### 1. Free port 80 and enable Nginx

Apache2 was holding `:80` with a default page and preventing Nginx from binding. Disabled Apache and enabled Nginx instead.

```bash
systemctl stop apache2
systemctl disable apache2
systemctl start nginx
systemctl enable nginx
```

### 2. Start gunicorn bound to loopback

```bash
cd /home/api/vasconcelos-api
source env/bin/activate
gunicorn core.wsgi:application --bind 127.0.0.1:9000 -D
```

Gunicorn is bound to `127.0.0.1:9000` so only Nginx can reach it.

### 3. Create Nginx vhost

Wrote `/etc/nginx/sites-available/api.vasconcelosagricola.com.br` and symlinked it into `sites-enabled/`. Final contents (after certbot):

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name api.vasconcelosagricola.com.br;

    if ($host = api.vasconcelosagricola.com.br) {
        return 301 https://$host$request_uri;
    } # managed by Certbot

    return 404;
}

server {
    listen 443 ssl; # managed by Certbot
    listen [::]:443 ssl; # managed by Certbot
    server_name api.vasconcelosagricola.com.br;

    ssl_certificate /etc/letsencrypt/live/api.vasconcelosagricola.com.br/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/api.vasconcelosagricola.com.br/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

    client_max_body_size 25m;

    location / {
        proxy_pass http://127.0.0.1:9000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable + reload:

```bash
ln -sf /etc/nginx/sites-available/api.vasconcelosagricola.com.br /etc/nginx/sites-enabled/
nginx -t && systemctl reload nginx
```

### 4. Issue Let's Encrypt certificate

```bash
certbot --nginx -d api.vasconcelosagricola.com.br \
  --non-interactive --agree-tos \
  -m rafaelricco10@gmail.com --redirect
```

Cert lives at `/etc/letsencrypt/live/api.vasconcelosagricola.com.br/`. Expires 2026-07-16.

### 5. Update Django trusted origins

In `core/settings.py`, appended `'https://api.vasconcelosagricola.com.br'` to both `CORS_ALLOWED_ORIGINS` and `CSRF_TRUSTED_ORIGINS`. Restarted gunicorn:

```bash
pkill -f "gunicorn core.wsgi"
env/bin/gunicorn core.wsgi:application --bind 127.0.0.1:9000 -D
```

`ALLOWED_HOSTS = ['*']` already accepts any host, so no change there.

## Verification

```bash
# DNS
getent hosts api.vasconcelosagricola.com.br
# → 147.79.81.43

# HTTP redirects to HTTPS
curl -sI http://api.vasconcelosagricola.com.br/ | head -2
# → HTTP/1.1 301 Moved Permanently

# HTTPS serves the Django API (DRF root → JSON with endpoint map)
curl -sI https://api.vasconcelosagricola.com.br/ | head -2
# → HTTP/1.1 200 OK
curl -s  https://api.vasconcelosagricola.com.br/ | head -1
# → {"products":"https://api.vasconcelosagricola.com.br/products/", ...}

# Certificate valid and matches the domain
echo | openssl s_client -servername api.vasconcelosagricola.com.br \
  -connect api.vasconcelosagricola.com.br:443 2>/dev/null \
  | openssl x509 -noout -subject -issuer -dates
# → subject=CN = api.vasconcelosagricola.com.br
# → issuer=... Let's Encrypt ...

# Gunicorn bound only to loopback (not publicly exposed)
ss -tlnp | grep 9000
# → 127.0.0.1:9000
```

## Renewal

Certbot's systemd timer handles renewals automatically:

```bash
systemctl list-timers | grep certbot    # snap.certbot.renew.timer (twice daily)
certbot renew --dry-run                  # optional: verify renewal works
```

No manual action required.

## Rollback

If the new domain needs to be disabled:

```bash
rm /etc/nginx/sites-enabled/api.vasconcelosagricola.com.br
nginx -t && systemctl reload nginx

# Optionally revert core/settings.py via git, then restart gunicorn
pkill -f "gunicorn core.wsgi"
env/bin/gunicorn core.wsgi:application --bind 127.0.0.1:9000 -D
```

Certificates can be left in place (harmless) or revoked:

```bash
certbot delete --cert-name api.vasconcelosagricola.com.br
```
