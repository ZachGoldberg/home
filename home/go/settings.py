import os
from home.settings import *

DEBUG = True

STATIC_URL = '/static/'

SITE_NAME = 'go.zachgoldberg.com'

SITE_BASE_URL = 'http://%s/' % SITE_NAME

REQUIRE_LOGIN = True
REQUIRE_VIEW_LOGIN = True

ROOT_URLCONF = 'home.go.urls'

APP_NAME = 'home.go'

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
SOURCE_ROOT = os.path.dirname(os.path.dirname(SITE_ROOT))
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'djangotoolbox',
    APP_NAME,
]
MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]


TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'rasdhasd%^&*asdawsje12 asdhavdbn!_)(*&'



if os.getenv("DJANGO_TOOLBAR"):
    MIDDLEWARE_CLASSES.append(
        'debug_toolbar.middleware.DebugToolbarMiddleware')
    INSTALLED_APPS.extend(['debug_toolbar',
                           'debug_toolbar_mongo'])
