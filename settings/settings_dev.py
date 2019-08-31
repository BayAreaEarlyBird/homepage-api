"""
Settings for development and local testing
"""

from settings.settings_common import *

DEBUG = True

ALLOWED_HOSTS = [
    'testserver',
    '127.0.0.1',
    'localhost',
    '0.0.0.0',
]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
