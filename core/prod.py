from .base import *
from dj_database_url import parse as dburl

ALLOWED_HOSTS = [ '*' ] # customize with your domain name

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {'default': config(
    'DATABASE_URL', default=default_dburl, cast=dburl), }

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "public/static")

MEDIA_URL = "/media/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_ROOT = os.path.join(BASE_DIR, "public/media")