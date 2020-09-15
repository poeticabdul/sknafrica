"""
Django settings for sheknowsnetwork project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8!3_@1)+*0=h+rrv9eu1z*55le8a9y*4bg_*clie+rwb8+1-)$'

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
    'django.contrib.sites',
    'skn_professionals',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_countries',
    'storages',
    
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sheknowsnetwork.urls'

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

WSGI_APPLICATION = 'sheknowsnetwork.wsgi.application'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
LOGIN_REDIRECT_URL = "/profile"
ACCOUNT_LOGOUT_REDIRECT_URL ='/accounts/login'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGOUT_ON_GET = True


AUTH_USER_MODEL = 'skn_professionals.User'


ACCOUNT_FORMS = {
    'signup': 'sheknowsnetwork.forms.CustomSignupForm',
}



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_ROOT = 'staticfiles'

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


if not DEBUG:

    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    S3_URL = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    STATIC_URL = S3_URL + 'static/'
    MEDIA_URL = S3_URL + 'media/'

    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')





# AWS_ACCESS_KEY_ID = "AKIA6LU5OBQ6VIRIXVBI"
# AWS_SECRET_ACCESS_KEY = "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"
# AWS_STORAGE_BUCKET_NAME = "sheknowsnetwork2"

# S3_URL = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# STATIC_URL = S3_URL + 'static/'
# MEDIA_URL = S3_URL + 'media/'

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SENDGRID_API_KEY = "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"

# STATICFILES_STORAGE = 'sheknowsnetwork.storage_backends.StaticStorage'

# DEFAULT_FILE_STORAGE = 'sheknowsnetwork.storage_backends.PublicMediaStorage'



EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' 
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'She Knows Network <info@sknafrica.com>'



# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if DEBUG:
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'sheknowsnetwork',
            'USER': 'poeticabdul',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

    STATIC_URL = '/static/'

    STATIC_ROOT = 'staticfiles'

    MEDIA_URL = '/media/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



django_heroku.settings(locals())


