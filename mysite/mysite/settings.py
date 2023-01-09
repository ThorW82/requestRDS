"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os, sys
import zoneinfo
from pathlib import Path

from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PROJECT_ROOT = os.path.dirname(__file__)
# sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rn_55y#+oif9=1rfazl&+55nq%@nwe@f3kwu@7!ra8*jcnndzc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.1.101', '192.168.1.109', 'localhost', '127.0.0.1', 'thorw.pythonanywhere.com']

# Application definition

INSTALLED_APPS = [
    'django_extensions',
    'debug_toolbar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'requestApp',
    'userprofile',

]

# AUTH_USER_MODEL = 'userprofile.User'

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 'whitenoise.middleware.WhiteNoiseMiddleware',
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ROOT_URLCONF = 'mysite.urls'

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

# WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ThorW$req',
        'USER': 'ThorW',
        'PASSWORD': '6Ubt!2iHJeW39jW',
        'HOST': 'localhost',
        # 'HOST': 'ThorW.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'uk'

# TIME_ZONE = 'GMT+2'
# TIME_ZONE = 'Europe/Kiev'
TIME_ZONE = 'EET'
# TIME_ZONE = 'UTC+2'


USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_ROOT = BASE_DIR / "staticfiles"



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 0,
        }
    },
]

LOGIN_URL = 'login'

USE_THOUSAND_SEPARATOR = True


INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# if settings.DEBUG:  # new
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# DEFAULT_FROM_EMAIL = 'admin@mail.com'
SERVER_EMAIL = "v.torishnyak@pharmasco.com"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = "mail.pharmasco.com"
EMAIL_HOST_USER = "v.torishnyak@pharmasco.com"
EMAIL_HOST_PASSWORD = 'jIQ1USKs'
# EMAIL_PORT = 587

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



# SMTPserver = "mail.pharmasco.com"
# sUsername = "v.torishnyak@pharmasco.com" ' Учетная запись на сервере
# sPass = "jIQ1USKs"    ' Пароль к почтовому аккаунту
# sFrom = sUsername'От кого