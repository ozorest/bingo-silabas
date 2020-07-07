"""
Django settings for bingo project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ
from django.core.management.utils import get_random_secret_key
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env(
    DJANGO_DEBUG=(bool, True),
    DJANGO_ALLOWED_HOSTS=(list, ['*']),
    DJANGO_DB_USE_S3=(bool, False),
    DJANGO_STATIC_USE_S3=(bool, False),
    DJANGO_MEDIA_ROOT=(str, os.path.join(BASE_DIR, "media")),
)

ENVIRONMENT = os.getenv('ENVIRONMENT')
if ENVIRONMENT == 'PRD':
    environ.Env.read_env()
elif ENVIRONMENT == 'DEV':
    environ.Env.read_env(env_file='.env.dev')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
random_secret_key = get_random_secret_key()
SECRET_KEY = random_secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DJANGO_DEBUG')

ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'django_s3_storage',
    'django_s3_sqlite',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bingo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'bingo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DJANGO_DB_USE_S3 = env('DJANGO_DB_USE_S3')

if DJANGO_DB_USE_S3:
    DATABASES = {
        'default': {
            'ENGINE': 'django_s3_sqlite',
            'NAME': env('AWS_DB_FILE'),
            "BUCKET": env('AWS_DB_BUCKET_NAME'),
        }
    }
else: 
    DATABASES = {
        'default': env.db('SQLITE_URL', default='sqlite://./data/bingo.sqlite3')
    }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# aws settings
DJANGO_STATIC_USE_S3 = env('DJANGO_STATIC_USE_S3')

if DJANGO_STATIC_USE_S3:
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_S3_BUCKET_NAME = env('AWS_S3_BUCKET_NAME')
    AWS_S3_BUCKET_NAME_STATIC = AWS_S3_BUCKET_NAME
    AWS_S3_KEY_PREFIX = "media"
    AWS_S3_KEY_PREFIX_STATIC = "static"
    AWS_REGION = env('AWS_REGION')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_S3_BUCKET_NAME}.s3.amazonaws.com'
    # s3 static settings
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    STATICFILES_STORAGE = 'django_s3_storage.storage.StaticS3Storage'
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage'
else:
    STATIC_URL = '/static/'
    MEDIA_ROOT = env('DJANGO_MEDIA_ROOT')

STATICFILES_DIRS = [
     os.path.join(BASE_DIR, "static"),
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'