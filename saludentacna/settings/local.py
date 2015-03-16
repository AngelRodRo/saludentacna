from .base import *
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'saludentacna',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '/Applications/MAMP/tmp/mysql/mysql.sock',
        'PORT': '3306',
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
MEDIA_ROOT = BASE_DIR.child('media')+'/'
MEDIA_URL = '/media/'
