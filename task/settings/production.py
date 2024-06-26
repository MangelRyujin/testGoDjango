from .base import *

# Debug Config
DEBUG =  True

# Allowed Hosts Config
ALLOWED_HOSTS = ["*"]

# Data Base config
DATABASES = {
    "default": {
        "ENGINE": config("ENGINE",default="django.db.backends.postgresql"),
        "NAME": config("DB_NAME", default="postgres"),
        "USER": config("DB_USER", default="postgres"),
        "PASSWORD": config("DB_PASSWORD", default="postgres"),
        "HOST": config("DB_HOST", default="127.0.0.1"),
        "PORT": config("DB_PORT", default=5432),
    }
}
