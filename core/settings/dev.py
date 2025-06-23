from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'skillupdb',
        'USER': 'mysql',
        'PASSWORD': 'mysql',
        'PORT': 3306,
    }
}
