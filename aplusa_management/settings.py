"""
Django settings for aplusa_management project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+*=#fk6hal!1g=97b%(2obmvq&&9l-h4rprwsq#1g5()hodm@j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.20.142']

# REST_FRAMEWORK={
#     'DEFAULT_AUTHENTICATION_CLASSES':[
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ],
# }

# SIMPLE_JWT={
#     'ACCESS_TOKEN_LIFETIME':timedelta(minutes=15)
# }


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'vehicle_type',
    'vehicle_mark',
    'vehicle_model',
    'vehicle',
    'accessory_model',
    'accessory_type',
    'accessory',
    'company_type',
    'company',
    'configuration',
    'department',
    'region',
    'simcard',
    'project',
    'price_type',
    'price',
    'job_title',
    'status',
    'person',
    'device_type',
    'device_mark',
    'device_model',
    'device_location',
    'device_detail',
    'device',
    'user',
    'user_permission'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aplusa_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'aplusa_management.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

filename = os.path.join(os.path.dirname(__file__), os.path.dirname(__file__).split("/")[-2]+"_configurations","db_name.txt")
db_name = open(filename).readlines()[0]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": db_name,
        "USER": "postgres",
        "PASSWORD": "VWw+$3!se5}%w68fZ2eX",
        "HOST": "localhost",
    }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL='/'

CORS_ORIGIN_WHITELIST='http://192.168.20.142:3000',
