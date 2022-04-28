import os
from pathlib import Path

import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

# should be changed
SECRET_KEY = os.getenv('SECRET_KEY', 'sk')
#SECRET_KEY = 'django-insecure-n64xhawv!!(h2)&@s&c!a%l-+w8jt56*i4f^2f0jnnr3sbdww#'
# random generated: EhNUk@DMJ#2JyhRWP5D%mbNSAZwc-4+),,Wpqqh-B?vKL5fxMEf5eFCmx)?65$a6

DEBUG = os.getenv('DEBUG', 'True')
# DEBUG = os.getenv('DEBUG', 'False') == 'True'
#DEBUG = True
APP_ENVIRONMENT = os.getenv('APP_ENVIRONMENT', 'Development')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(' ')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'project.accounts',
    'project.main',
    'project.weather',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'project.wsgi.application'

# should be changed
# DATABASES = None

DEFAULT_DATABASE_CONFIG = {
    'ENGINE': 'django.db.backends.postgresql',
    'HOST': os.getenv('DB_HOST', '127.0.0.1'),
    'PORT': os.getenv('DB_PORT', '5432'),
    'NAME': os.getenv('DB_NAME', 'actNews_db'),
    'USER': os.getenv('DB_USER', 'postgres'),
    'PASSWORD': os.getenv('DB_PASSWORD', '1123QwER'),
}

DATABASES = {
    'default': DEFAULT_DATABASE_CONFIG,
}

# should be changed
AUTH_PASSWORD_VALIDATORS = []

if APP_ENVIRONMENT == 'Production':
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR / 'static',
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = BASE_DIR, 'media/'
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING_LEVEL = 'DEBUG'

if APP_ENVIRONMENT == 'Production':
    LOGGING_LEVEL = 'INFO'
elif APP_ENVIRONMENT == 'Test':
    LOGGING_LEVEL = 'CRITICAL'

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'level': LOGGING_LEVEL,
            'filters': [],
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': LOGGING_LEVEL,
            'handlers': ['console'],
        },
    },
}

AUTH_USER_MODEL = 'accounts.ActNewsUser'

cloudinary.config(
  cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME', None),
  api_key = os.getenv('CLOUDINARY_API_KEY', None),
  api_secret = os.getenv('CLOUDINARY_API_SECRET', None)
)