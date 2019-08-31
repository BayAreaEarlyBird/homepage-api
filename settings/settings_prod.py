"""
Settings for production environment
"""

from settings.settings_common import *

DEBUG = False

ALLOWED_HOSTS = [
    'bayareaearlybird.com',
]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'homepage_prod',
        'USER': 'dbuser',
        'PASSWORD': 'zaoniaodb123',
        'HOST': 'localhost',
        'PORT': '',
    }
}
