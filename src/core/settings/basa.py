from .local import *
from pathlib import Path
from .jazzmin import JAZZMIN_SETTINGS , JAZZMIN_UI_TWEAKS
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent



TEME_PARTY_APPS = [
    'debug_toolbar',
]


APPS = [
    'catalog'
]


THEME = [
    'jazzmin'
]

INSTALLED_APPS = [
    *TEME_PARTY_APPS,
    *THEME,
    'django.contrib.admin',
    'django.contrib.auth', # Фреймворк аутентификации и моделей по умолчанию.
    'django.contrib.contenttypes', # Django контент-типовая система (даёт разрешения, связанные с моделями).
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_memcached',
    *APPS
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # Управление сессиями между запросами
    'django.contrib.sessions.middleware.SessionMiddleware', # Управление сессиями между запросами
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Связывает пользователей, использующих сессии, запросами.
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'


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



INTERNAL_IPS = [
   "127.0.0.1", "*"
]


ALLOWED_HOSTS = ['*']

LANGUAGE_CODE = 'en-us'

# Перенаправление на домашний URL-адрес после входа в систему (по умолчанию перенаправление на /accounts/profile/)
LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'catalog', 'static')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



CACHES = {
    "default": {
        "BACKEND":"django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION":"memcached:11211"
    }
}

# File-based caching 

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',  # Укажите путь к каталогу, где будут храниться файлы кэша
    }
}