import os
from environs import Env
import dj_database_url


env = Env()
env.read_env()


DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
    }
}
DATABASES['default'] = dj_database_url.config(
    default='postgres://USER:PASSWORD@HOST:PORT/NAME',
    conn_max_age=600,
    conn_health_checks=True,
)


INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
