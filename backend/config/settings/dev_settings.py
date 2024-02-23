from config.settings.base_settings import *

INSTALLED_APPS += [
    "debug_toolbar",  # django debug toolbar package
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # debug toolbar
]

INTERNAL_IPS = [
    # debug toolbar
    "0.0.0.0",
]

REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"].append(
    "rest_framework.authentication.SessionAuthentication"
),
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"].append(
    "rest_framework.renderers.BrowsableAPIRenderer"
)

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    # Toolbar options
    "RESULTS_CACHE_SIZE": 3,
    "SHOW_COLLAPSED": True,
    # Panel options
    "SQL_WARNING_THRESHOLD": 100,  # milliseconds
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}
