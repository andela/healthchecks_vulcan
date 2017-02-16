import os

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     'hc',
        'USER':     'brianmuthui',
        'PASSWORD': '',
        'TEST': {'CHARSET': 'UTF8'}
    }
}

DJMAIL_REAL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = bool(os.environ.get("EMAIL_USE_TLS"))
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT"))
SITE_ROOT = 'http://healthchecks-vulcan.herokuapp.com'
HOST = 'healthchecks-vulcan.herokuapp.com'
