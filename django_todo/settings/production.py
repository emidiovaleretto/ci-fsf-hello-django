from .settings import *
from decouple import config
import dj_database_url

DEBUG = config("DEBUG")
SECRET_KEY = config("SECRET_KEY_PRODUCTION")
HOST = config("HOST")
POSTGRES_DB = config("POSTGRES_DB")

# ALLOWED_HOSTS
ALLOWED_HOSTS=[HOST]

DATABASES = {
    'default': dj_database_url.parse(POSTGRES_DB)
}