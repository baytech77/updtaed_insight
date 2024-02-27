"""
Django settings for insight_voice project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import django_heroku
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0tjk1+u9qamb2u-vaax2g3otp#pi_h6e60jy@7armn-#n2ldnd'

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
    'rest_framework',
    # installed apps for the project
    'home_app.apps.HomeAppConfig',
    'user_account.apps.UserAccountConfig',
    'user_app.apps.UserAppConfig',
    'article.apps.ArticleConfig',
    'api.apps.ApiConfig',
    # for editing the forms
    'crispy_forms',
    'crispy_tailwind',
    # Reloader for tailwind
    'django_browser_reload',
    # installed app for template designs
    'tailwind',
    'theme',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # for reload asychronosity
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]

ROOT_URLCONF = 'insight_voice.urls'

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

WSGI_APPLICATION = 'insight_voice.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'insight_database',
        'USER': 'postgres',
        'PASSWORD': 'BAYu@1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# static files config
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# media configuration
MEDIA_URL = 'media/'
MEDIAFILES_DIRS = [os.path.join(BASE_DIR, 'media')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# User ridirect
LOGIN_REDIRECT_URL = 'home_app:home'
LOGOUT_REDIRECT_URL = 'home_app:landing'

# user models
AUTH_USER_MODEL = 'user_app.CustomUser'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = ["127.0.0.1"]
NPM_BIN_PATH = r"c:/Program Files/nodejs/npm.cmd"
CRISPY_ALLOWED_TEMPLATE_PACKS = 'tailwind'
CRISPY_TEMPLATE_PACK = 'tailwind'
# email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


TIME_ZONE = 'America/New_York'

# setting Heroku
django_heroku.settings(locals())
 
# CSRF_COOKIE_NAME = 'csrftoken'
# CSRF_COOKIE_AGE = 60 * 60 * 24 * 7 * 2  # Two weeks
# CSRF_COOKIE_SECURE = False
# CSRF_COOKIE_HTTPONLY = True
# CSRF_COOKIE_PATH = '/'
# CSRF_COOKIE_DOMAIN = None
# CSRF_TRUSTED_ORIGINS = ['']
# CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'