from django.conf import settings
from .base import *

ALLOWED_HOSTS = ['localhost' ,'127.0.0.1']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:8000",
]
CORS_ORIGIN_ALLOW_ALL = False
DEFAULT_PORT = 8000
ENV_ROLE='dev'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True