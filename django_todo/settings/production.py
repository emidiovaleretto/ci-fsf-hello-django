from .settings import *
from decouple import config
import dj_database_url

DEBUG = config("DEBUG")
SECRET_KEY = config("SECRET_KEY_PRODUCTION")
POSTGRES_DB = config("POSTGRES_DB")

# ALLOWED_HOSTS
ALLOWED_HOSTS=['localhost', '127.0.0.1']

DATABASES = {
    'default': dj_database_url.parse(POSTGRES_DB)
}