"""
Django settings for travelproject project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b&6sfre4_-2miw*x1hpnob*6rt0!yf+k1(c8$8ct9sgdsxvh$1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'travelapp.apps.TravelappConfig',
    'drf_yasg',
    'rest_framework',
    'debug_toolbar',
    'oauth2_provider',
    'corsheaders',
    'social_django', # login facebook
    'drf_social_oauth2',# login facebook
    'ckeditor',
    'ckeditor_uploader',
]

CKEDITOR_UPLOAD_PATH = "images/ckeditor/"
MEDIA_ROOT = '%s/travelapp/static/' % BASE_DIR
STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        # login facebook
        'drf_social_oauth2.authentication.SocialAuthentication',
    )
}

# login facebook
AUTHENTICATION_BACKENDS = (
    # Facebook OAuth2
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

    # drf_social_oauth2
    'drf_social_oauth2.backends.DjangoOAuth2',

    # Django
    'django.contrib.auth.backends.ModelBackend',
)

# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = '<your app id goes here>'
SOCIAL_AUTH_FACEBOOK_SECRET = '<your app secret goes here>'

# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from Facebook.
# Email is not sent by default, to get it, you must request the email permission.
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOW_METHODS = ["DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT"]
# CORS_ALLOW_ORIGINS = ["https://example.com", "https://sub.example.com"]

INTERNAL_IPS = [
    '127.0.0.1'
]

ROOT_URLCONF = 'travelproject.urls'

OAUTH2_INFO = {
    "id": 'Tv69E4q1eCW6Ot0oFTveJRvTFrMJAXSsLuvYP93x',
    "secret": 'huCxBhEpbeIBVqypg2nBeE0nV8XJ8iCxpP9fdjLvPuS0ntIwAEHqFjbh0WxNe1KoOWjsL8yNYHnFBfT1D55OO0ywduGyTzwH5gDMY8IPSb6fupBYsocU9h3tHZvv7nB8'
}

# OAUTH2_PROVIDER = {
#
# }

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
                # login facebook
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


WSGI_APPLICATION = 'travelproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travelappdb',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': ''  # mặc định localhost
    }
}

import pymysql
pymysql.install_as_MySQLdb()

AUTH_USER_MODEL = 'travelapp.User'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

