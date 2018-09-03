from .common import *
from django_secret_key import secret_key

DEBUG = True
SECRET_KEY = secret_key
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

from postgres_prod import postgres_details
DATABASES = {
    'default': postgres_details
}
