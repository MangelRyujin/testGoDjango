from .base import *


# Debug Config
DEBUG =  config("DEBUG", default=True, cast=bool)



# Allowed Hosts Config
ALLOWED_HOSTS = ["*"]



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
