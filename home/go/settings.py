from wifast.settings import *

SITE_NAME = 'links.wifast.com'

SITE_BASE_URL = 'http://%s/' % SITE_NAME

REQUIRE_LOGIN = True
REQUIRE_VIEW_LOGIN = True

ROOT_URLCONF = 'wifast.links.urls'

APP_NAME = 'wifast.links'

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

MIDDLEWARE_CLASSES = BASE_MIDDLEWARE_CLASSES

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)


if os.getenv("DJANGO_TOOLBAR"):
    MIDDLEWARE_CLASSES.append(
        'debug_toolbar.middleware.DebugToolbarMiddleware')
    INSTALLED_APPS.extend(['debug_toolbar',
                           'debug_toolbar_mongo'])
