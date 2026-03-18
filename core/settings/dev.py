from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


INSTALLED_APPS += [
    'debug_toolbar',
    'whitenoise.runserver_nostatic',
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
INTERNAL_IPS = ['127.0.0.1']

# Email (backend console for development)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
