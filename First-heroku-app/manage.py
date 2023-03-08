# NOTE: This is all boilerplate, don't edit this file!! (Still run it, however)
import sys
import os
from django.conf import settings
from django.core.management import execute_from_command_line

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DEBUG=True,
    ROOT_URLCONF='urls',
    STATIC_URL='static/',
    STATICFILES_DIRS=[os.path.join(BASE_DIR, "static")],
    SECRET_KEY='rre1h#l@&z!zcbg',
    ALLOWED_HOSTS=['*'],
    INSTALLED_APPS=[
        'django.contrib.staticfiles',
    ],
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    }],
)

execute_from_command_line(sys.argv)
