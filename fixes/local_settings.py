import os
from settings import *

KOBOCAT_URL = os.environ.get('KOBOCAT_URL','http://localhost:8001')
FORGOT_PASSWORD_URL = KOBOCAT_URL + '/accounts/password/reset/'
KOBOCAT_INTERNAL_URL = os.environ.get('KOBOCAT_INTERNAL_URL','http://fieldsight:8001')


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('POSTGRES_DB','fieldsight'),
        'USER': os.environ.get('POSTGRES_USER', 'fieldsight'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'fieldsight'),
        'HOST': os.environ.get('POSTGRES_HOST','postgis'),
        'PORT': os.environ.get('POSTGRES_PORT','5432'),
    }
}

MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware']

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')
SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME','my_cookie')
SESSION_COOKIE_DOMAIN = os.environ.get('SESSION_COOKIE_DOMAIN', '.localhost')

os.environ["ENKETO_VERSION"] = "Express"
ENKETO_URL = os.environ.get('ENKETO_URL', 'http://localhost:8005/')

ENKETO_SERVER = os.environ.get('ENKETO_URL') or os.environ.get('ENKETO_SERVER', 'http://localhost:8005/')
ENKETO_SERVER= ENKETO_SERVER + '/' if not ENKETO_SERVER.endswith('/') else ENKETO_SERVER
ENKETO_VERSION= os.environ.get('ENKETO_VERSION', 'Legacy').lower()
#assert ENKETO_VERSION in ['legacy', 'express']
ENKETO_PREVIEW_URI = 'webform/preview' if ENKETO_VERSION == 'legacy' else 'preview'

DEFAULT_DEPLOYMENT_BACKEND = 'kobocat'

BROKER_URL = "redis://redis_main:6379/0"

DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True

CORS_URLS_REGEX = r'^/assets/.*$'

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'jsapp/compiled/',
        'POLL_INTERVAL': 0.5,
        'TIMEOUT': 5,
    }
}


MONGO_DATABASE = {
    'HOST': os.environ.get('MONGO_HOST', 'localhost'),
    'PORT': int(os.environ.get('MONGO_PORT', 27017)),
    'NAME': os.environ.get('MONGO_NAME', 'abc'),
    'USER': os.environ.get('MONGO_USER', ''),
    'PASSWORD': os.environ.get('MONGO_PASS', '')
}

if MONGO_DATABASE.get('USER') and MONGO_DATABASE.get('PASSWORD'):
    MONGO_CONNECTION_URL = (
        "mongodb://%(USER)s:%(PASSWORD)s@%(HOST)s:%(PORT)s") % MONGO_DATABASE
else:
    MONGO_CONNECTION_URL = "mongodb://%(HOST)s:%(PORT)s" % MONGO_DATABASE

MONGO_CONNECTION = MongoClient(
    MONGO_CONNECTION_URL, j=True, tz_aware=True, connect=False)
MONGO_DB = MONGO_CONNECTION[MONGO_DATABASE['NAME']]

print ("end of localsettings")