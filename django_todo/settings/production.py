import os
from .settings import *
import dj_database_url

if os.path.exists('env.py'):
    import env

DEBUG = os.environ.get("DEBUG")
SECRET_KEY = os.environ.get("SECRET_KEY_PRODUCTION")
HOST = os.environ.get("HOST")
POSTGRES_DB = os.environ.get("POSTGRES_DB")

# ALLOWED_HOSTS
ALLOWED_HOSTS=[HOST]

DATABASES = {
    'default': dj_database_url.parse(POSTGRES_DB)
}