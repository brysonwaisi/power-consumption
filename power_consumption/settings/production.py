from django.conf import settings
from .base import *

ALLOWED_HOSTS = ['greenie.com/']

CORS_ALLOWED_ORIGINS = [
    'https://greenie.com'
]
# CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [ 'https://greenie.com' ]

DEFAULT_PORT = 9035
ENV_ROLE='prod'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False