# noinspection PyUnresolvedReferences
from .default import *
import dj_database_url

DEBUG = True
ALLOWED_HOSTS = ['*']

# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': env.str('DB_NAME'),
#         'USER': env.str('DB_USER'),
#         'PASSWORD': env.str('DB_PASSWORD'),
#         'HOST': env.str('DB_HOST'),
#         'PORT': env.str('DB_PORT'),
#     }
# }

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

