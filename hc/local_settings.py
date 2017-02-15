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
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'muthuimbrian@gmail.com'
EMAIL_HOST_PASSWORD = "hunters17BILU"
EMAIL_PORT = 587