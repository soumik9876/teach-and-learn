# noinspection PyUnresolvedReferences
from .default import *
import dj_database_url

DEBUG = True
ALLOWED_HOSTS = ["teach-and-learn-api.herokuapp.com", "0.0.0.0:8000", 'localhost', '127.0.0.1']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "d6fbeqg7n9s9ot",
        'USER': "dxwkkduepohfkg",
        'PASSWORD': 'cd8c3748d8c292c089affbf62864b802e5f6909cadbfb461521bc0aa3fd13032',
        'HOST': 'ec2-3-228-78-248.compute-1.amazonaws.com',
        'PORT': "5432",
    }
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [BASE_DIR / 'static_local']

# DEBUG TOOLBAR
INTERNAL_IPS = []

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

