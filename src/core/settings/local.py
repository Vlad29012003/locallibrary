from .basa import *
from pathlib import Path
from decouple import config as env


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOST = env('ALLOWED_HOSTS',default='localhost').split(',')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST' , default ='db'),
        'PORT': env('POSTGRES_PORT' ,default ='5432' ,cast=int)
    }
}
