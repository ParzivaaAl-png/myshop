from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------------
# BASIC SETTINGS
# -------------------------------------------------------------------
SECRET_KEY = 'django-insecure-1234567890-replace-in-production'
DEBUG = True

ALLOWED_HOSTS = ['*']  # локальная разработка + Render


# -------------------------------------------------------------------
# INSTALLED APPS
# -------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'products',
]


# -------------------------------------------------------------------
# MIDDLEWARE
# -------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# -------------------------------------------------------------------
# URLS + WSGI
# -------------------------------------------------------------------
ROOT_URLCONF = 'shop.urls'

WSGI_APPLICATION = 'shop.wsgi.application'


# -------------------------------------------------------------------
# TEMPLATES
# -------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # важное место! подключаем templates/
        'DIRS': [
            BASE_DIR / 'templates',
        ],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# -------------------------------------------------------------------
# DATABASE
# -------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Если мы будем использовать Render PostgreSQL — я добавлю поддержку через dj-database-url


# -------------------------------------------------------------------
# AUTH & PASSWORDS
# -------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# -------------------------------------------------------------------
# LANGUAGE + TIMEZONE
# -------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# -------------------------------------------------------------------
# STATIC FILES & MEDIA
# -------------------------------------------------------------------

# STATIC
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',   # твои CSS, JS, images
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # для продакшна (Render, etc)

# MEDIA — изображения товаров
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# -------------------------------------------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# -------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
