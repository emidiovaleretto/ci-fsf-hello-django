import os
from .settings import *
import dj_database_url

if os.path.exists('env.py'):
    import env

DEBUG = os.environ.get("DEBUG")
SECRET_KEY = os.environ.get("SECRET_KEY_PRODUCTION")

# ALLOWED_HOSTS
ALLOWED_HOSTS=[
    os.environ.get("HEROKU_HOST")
]

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("HEROKU_DB"))
}