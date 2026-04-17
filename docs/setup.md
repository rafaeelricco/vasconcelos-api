# Vasconcelos API - Setup Guide

> For the public-domain / HTTPS production setup, see [setup-domain.md](./setup-domain.md).

## Prerequisites

- Python 3.9+ with virtual environment at `env/`
- Docker installed
- Dependencies installed via `pip install -r requirements.txt`

## 1. Start Redis (via Docker)

The application uses Redis for caching. Start it as a Docker container:

```bash
docker run -d --name redis \
  --restart unless-stopped \
  -p 6379:6379 \
  redis:7 --requirepass yechEb7n
```

Verify Redis is running:

```bash
docker exec redis redis-cli -a yechEb7n ping
# Expected: PONG
```

## 2. Activate Virtual Environment

```bash
cd /home/api/vasconcelos-api
source env/bin/activate
```

## 3. Run Migrations

```bash
python manage.py migrate
```

## 4. Start the Application

### Background (daemon) mode:

```bash
gunicorn core.wsgi:application --bind 0.0.0.0:9000 -D
```

### Foreground mode - useful for debugging:

```bash
gunicorn core.wsgi:application --bind 0.0.0.0:9000
```

## 5. Verify

```bash
# Check Redis
docker exec redis redis-cli -a yechEb7n ping

# Check gunicorn processes
ps aux | grep gunicorn

# Check port 9000
ss -tlnp | grep 9000

# Test HTTP response
curl -s -o /dev/null -w "%{http_code}" http://localhost:9000/
```

## Stopping Services

```bash
# Stop gunicorn
pkill gunicorn

# Stop Redis
docker stop redis && docker rm redis
```

## Configuration

| Setting | Value |
|---------|-------|
| Application port | `0.0.0.0:9000` |
| Redis host | `127.0.0.1:6379` |
| Redis DB | `1` |
| Database | SQLite (`db.sqlite3`) or PostgreSQL via `DATABASE_URL` env var |
| Static files | `public/static/` |
| Media files | `public/media/` |
| Django settings | `core/settings.py` |
| Environment vars | `.env` |
