import os
import socket

IS_PROD = True

## Django's Debug Toolbar
DEBUG_TOOLBAR_MONGO_STACKTRACES = not IS_PROD
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': lambda x: True,
    'ENABLE_STACKTRACES': DEBUG_TOOLBAR_MONGO_STACKTRACES,
}

import copy
import logging
import os
import sys

APP_NAME = 'home.go'
SITE_ROOT = os.path.join(os.path.dirname(os.path.dirname(
    os.path.realpath(__file__))), "go")
SOURCE_ROOT = os.path.dirname(os.path.dirname(SITE_ROOT))

TESTING = sys.argv[1:2] == ['test']

DEBUG = True
TASTYPIE_FULL_DEBUG = DEBUG
TEMPLATE_DEBUG = DEBUG
IS_PROD = False
IS_DEV = False

ADMINS = (
    ('Zach Goldberg', 'zach@zachgoldberg.com'),
)

MANAGERS = ADMINS

LOCAL_MONGO_DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'wifastportal',
        'USER': 'wifast',
        'PASSWORD': 'wifast2458',
        'HOST': 'localhost',
        'PORT': 27017,
        # don't use eventual consistency locally
        # so we can catch integrity errors more easily
        # (saves a ton of time for debugging)
        'OPTIONS': {
            'safe': True,
        },
    },
}

LOGIN_URL = "/"

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',  # django_compressor
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'r24qw^nw1+7zr!%x4ze4%gn_yz0b@zudbi$5&pv=0v*!y9_ju)'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# TODO: refactor this all so that children apps (sites, etc)
# inherit from base and dont override things from here
BASE_MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'wifast.portal.utils.context_processors.product_info',
    'wifast.portal.utils.context_processors.prod_environment',
    'wifast.portal.utils.context_processors.csrf_token',
    # requested by Facebook integration
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'wifast.portal.urls'

TEMPLATE_DIRS = (
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'templates'),
    os.path.join(
        os.path.join(os.path.dirname(SITE_ROOT), 'routerconfiguration'),
        'templates')
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'djangotoolbox',
    'url_shortener',
    APP_NAME,
]

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    'debug_toolbar_mongo.panel.MongoDebugPanel',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'ERROR',
            'propagate': True,
        }
    }
}


def add_toolbar():
    # Debug toolbar slows down tests like nobody's business,
    # so only let it run locally
    MIDDLEWARE_CLASSES.append(
        'debug_toolbar.middleware.DebugToolbarMiddleware')
    INSTALLED_APPS.extend(['debug_toolbar',
                           'debug_toolbar_mongo'])

