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
import hoover
import logging
import os
import sys

APP_NAME = 'wifast.portal'
LOGGING_APP_NAME = 'wifast.logging'
REX_APP_NAME = 'wifast.rex'
BLOCKSITE_APP_NAME = 'wifast.blocksite'
ROUTERUPDATE_APP_NAME = 'wifast.routerupdate'
IMAGESERVER_APP_NAME = 'wifast.imageserver'

DEV_URLS = "wifastdev.com"

PROD_URL = "portal.wifast.com"
SMBSITE_URL = "bizsite.wifast.com"
CEREBRO_URL = "jenkins.wifast.com:30000"
REX_URL = "rex.wifast.com"
LOGGING_URL = "logging.wifast.com"
ROUTERAPI_URL = "routerapi.wifast.com"
ROUTERUPDATE_URL = "routerupdate.wifast.com"
WIFIWIND_PORTAL_URL = "portal.wifiwind.com"
WIFAST_HOMEPAGE = "www.wifast.com"


ROUTERUPDATE_USER = 'routerupdate'
# User-Agents that we know spam us a bunch
# and create lots of extra accessdevices.  When
# We see one of these we will avoid making
# new accessdevices
USERAGENT_BLACKLIST = [
    "Debian APT-HTTP",
    'NewRelicPinger',
    'Microsoft NCSI',
    'AndroidDownloadManager',
    'Unknown',
    'CaptiveNetworkSupport',
    'curl-agent',
    'Apple-PubSub/65.28',
    'Skype WISPr',
    'Twitter',
]

PRODUCT_NAME = 'WifiWind'
PRODUCT_NAME_HTML = 'Wifi<strong>Wind</strong>'
PRODUCT_VERSION = 'v2'


API_SECRET_KEY = 'staceysmomhasgotitgoingon'
NT_HASH_KEY = '995e19386b876dde53d618c1b95baa8a'

KISSMETRICS_API_KEY = 'fa1402d5762fb55229993cc9736c1307d47103c7'

GATEWAY_IP = "172.19.245.1"
GATEWAY_PORT = "2060"

RADIUS_SECRET_KEY = 'RADIUSKEY'
RADIUS_ADDRESS = '1.2.3.4'
RADIUS_PORT = '1234'

PRIVATE_LAN_IPADDR = '172.18.245.1'
WIFAST_LAN_IPADDR = '172.19.245.1'

OFFICE_IPADDRESSES = ['50.143.172.93']

GAE_KEY = 'qweasdzxc'
GAE_URL = "localhost:8080"
PROD_GAE_URL = "wifastrex.appspot.com"

FIRMWARE_URL = "https://s3-us-west-1.amazonaws.com/wf-firmware-deployment"

SITE_ROOT = os.path.join(os.path.dirname(os.path.dirname(
    os.path.realpath(__file__))), "portal")
SOURCE_ROOT = os.path.dirname(os.path.dirname(SITE_ROOT))

TESTING = sys.argv[1:2] == ['test'] or os.getenv('WIFAST_TESTING')

DEBUG = True
TASTYPIE_FULL_DEBUG = DEBUG
TEMPLATE_DEBUG = DEBUG
IS_PROD = False
IS_DEV = False


# Twilio account details for blockapp marketing
BLOCKAPP_TWILIO_PARAMS = {
    "auth_token": '6c4efbd186bdafa25f29bc96814c5eef',
    "api_version": '2010-04-01',
    "from_number": '+14156399930',
    "sid": 'ACf1411372d1fefaf18081ee5ea7fa5774',
}


# Hosting catserver & DNSServer in the same place for now
ADBLOCK_DNS = "50.112.249.130"
ADBLOCK_NOADSERVER_IP = "50.112.249.130"

NOADS_DNS_SERVERS = ["54.245.84.240"]
CAT_DNS_SERVERS = ["50.112.249.130"]

ADMINS = (
    ('WiFast Engineering Team', 'engineering@wifast.com'),
)

MANAGERS = ADMINS
DETECTION_METRICS_RECIPIENTS = "dailymetrics@wifast.com"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'production@wifast.com'
CHRONOGRAPH_EMAIL_SENDER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = 'QWE123qwe123'
EMAIL_USE_TLS = True
SERVER_EMAIL = 'production@wifast.com'
USEROPS_EMAIL = 'userops@wifast.com'

TEST_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite
        'NAME': '/mnt/data/hosts.db',
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '',
        # Set to empty string for default. Not used with sqlite3.
        'PORT': '',
    },
}


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

PROD_DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'wifastportal',
        # TODO Auth with Mongo
        'USER': 'wifast',
        'PASSWORD': 'wifast2458',
        'HOST': ['0.aws-us-west-2a.mongodb.wifast.com',
                 '1.aws-us-west-2a.mongodb.wifast.com',
                 '0.aws-us-west-1b.mongodb.wifast.com'],
        'PORT': 27017,
    },
}

LOCAL_TUNNEL_PROD_DATABASES = copy.deepcopy(PROD_DATABASES)
LOCAL_TUNNEL_PROD_DATABASES['default']['PORT'] = 9999
LOCAL_TUNNEL_PROD_DATABASES['default']['HOST'] = 'localhost'

USING_NOSQL = True
FIXTURE_DIRS = (SITE_ROOT + '/fixtures/nosql/',)

LOGIN_URL = "/"
ORIG_URL_NAME = 'wfst_orig_url_rdr'
ACCESSDEVICE_COOKIE_ID_NAME = 'wfst_ad_id'

WHITELISTED_DOMAINS = []

INTERNAL_IPS = ['127.0.0.1']

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

b

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
    # for django-socialregistration
    'django.contrib.sites',
    'socialregistration',
    'socialregistration.contrib.facebook',
    'tastypie',
    'compressor',   # django_compressor
    'chronograph',  # django-chronograph
    'url_shortener',
    REX_APP_NAME,
    LOGGING_APP_NAME,
    ROUTERUPDATE_APP_NAME,
    BLOCKSITE_APP_NAME,
    IMAGESERVER_APP_NAME,
    APP_NAME,
    'wifast.dnsserver',
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

AUTH_PROFILE_MODULE = 'portal.UserProfile'
AUTHENTICATION_BACKENDS = (
    'wifast.portal.backends.CaseInsensitiveModelBackend',
    'socialregistration.contrib.facebook.auth.FacebookAuth',
)

FACEBOOK_REQUEST_PERMISSIONS = 'email'

# for sites framework - just created one for wifiwind for now
SOCIALREGISTRATION_GENERATE_USERNAME = True

# Mailgun settings
MAILGUN_API_KEY = "key-76ve4stlzng1f21w0iqknkjppkggrid4"

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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

## Stripe
STRIPE_SECRET_KEY = "BjM1wiDeyXrVQMVJZ6kLmnjYdpPxuYLQ"
STRIPE_PUBLISHABLE_KEY = "pk_Zm1CRl0w9PSjPchGXDtuYi21RA2DH"

# Loggly logging
LOGGLY_HANDLER = hoover.LogglyHttpHandler(
    token='00126189-9527-4acc-b5a1-bad104a0bffb')

IOS_CLIENT_NAMES = ['Block 1.1 (iOS)', 'Block 12 (iOS)', 'Block 1.3.1 (iOS)']

# CatBlock adding clients to be monitored
WILD_CLIENT_NAMES = [
    'WiFast-Android-Block-0.%s' % i for i in range(6, 22, 2)
]

WILD_CLIENT_NAMES += ['Android-Block-0.%s' % i for i in range(22, 142, 2)]

WILD_CLIENT_NAMES += ['WiFast-Android-Block-0.3']

ANDROID_CLIENT_NAMES = WILD_CLIENT_NAMES

# For now we want to remove iOS clients while that data
# is so skewed.
#WILD_CLIENT_NAMES += IOS_CLIENT_NAMES

WILD_ROMNEY_CLIENT_NAMES = [
    'Android-Romney-Block-0.%s' % i for i in range(2, 20, 2)
]

WILD_OBAMA_CLIENT_NAMES = ['Android-Obama-0.%s' % i for i in range(2, 20, 2)]

# prod will override this to only show even (non-dev) app versions
ANDROID_EVENTLOG_V2_VERSIONS = set(str(ver) for ver in range(66, 998))

IDENTIFIER_CLIENT = 'Logging-Identifier'

UNAUTH_IDENTIFIER = 'Unauthenticated-Identifier'

UNNATURAL_CLIENTS = [IDENTIFIER_CLIENT, UNAUTH_IDENTIFIER]


def setup_loggly(logger):
    logger.addHandler(LOGGLY_HANDLER)
    logger.setLevel(logging.INFO)

# Watchdog is enabled by default, to temporarily disable, set to False:
DOGSLOW = True

# Location where Watchdog stores its log files:
DOGSLOW_OUTPUT = '/tmp'

# Log requests taking longer than 25 seconds:
DOGSLOW_TIMER = 25

# When both specified, emails backtraces:
DOGSLOW_EMAIL_TO = 'engineering@wifast.com'
DOGSLOW_EMAIL_FROM = 'team-notices@wifast.com'

# Also log to this logger (defaults to none):
DOGSLOW_LOGGER = 'syslog_logger'
DOGSLOW_LOG_LEVEL = 'WARNING'

# Tuple of url pattern names that should not be monitored:
# (defaults to none -- everything monitored)
# DOGSLOW_IGNORE_URLS = ('some_view', 'other_view')

# Print (potentially huge!) local stack variables (on by default, use
# False for less detailed, but more manageable reports)
DOGSLOW_STACK_VARS = True
