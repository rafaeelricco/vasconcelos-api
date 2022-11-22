import os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = [
    config("ALLOWED_TO_DEV"),
    config("ALLOWED_TO_PROD"),
    config("ALLOWED_TO_STAGING"),
    config("ALLOWED_TO_TEST"),
]

INSTALLED_APPS = [
    "admin_interface",
    "colorfield",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "easy_thumbnails",
    "corsheaders",
    "text_block",
    "categories",
    "consortium",
    "products",
    "ckeditor",
    "banners",
    "parts",
    "filer",
    "useds",
    "core",
]

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

CORS_ALLOWED_ORIGINS = [
    config("CORS_ALLOWED_ORIGINS_DEV"),
    config("CORS_ALLOWED_ORIGINS_PROD"),
    config("CORS_ALLOWED_ORIGINS_LOCAL"),
    config("CORS_ALLOWED_ORIGINS_STAGING"),
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"
SESSION_ENGINE = "django.contrib.sessions.backends.cache"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_NAME"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST"),
        "PORT": config("POSTGRES_PORT"),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config("REDIS_HOST"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"

MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, "storage/static")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_ROOT = os.path.join(BASE_DIR, "storage/media")

FILER_STORAGES = {
    "public": {
        "main": {
            "ENGINE": "filer.storage.PublicFileSystemStorage",
            "OPTIONS": {
                "location": f"{MEDIA_ROOT}/images",
                "base_url": f"{MEDIA_URL}/images",
            },
            "UPLOAD_TO_PREFIX": "file",
        },
        "thumbnails": {
            "ENGINE": "filer.storage.PublicFileSystemStorage",
            "OPTIONS": {
                "location": f"{MEDIA_ROOT}/tmp/thumbnails",
                "base_url": f"{MEDIA_URL}/tmp/thumbnails/",
            },
        },
    },
}
