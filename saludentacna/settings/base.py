# -*- encoding: utf-8 -*-
from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = '^5*+7oa2$b*as@s#7w2dfup$e#^pt*&v98=6*ebbvvd@ygbz+&'

DJANGO_APPS = (

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS =(
    'PIL',

)
LOCAL_APPS = (
    'apps.users',
    'apps.clinics',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'saludentacna.urls'

WSGI_APPLICATION = 'saludentacna.wsgi.application'

LANGUAGE_CODE = 'es-pe'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [ BASE_DIR.child('templates')]

AUTH_USER_MODEL = 'users.User'