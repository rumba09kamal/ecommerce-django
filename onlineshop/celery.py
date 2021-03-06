import os
from celery import Celery
from django.conf import settings

# set the default django settings module for the celery program
os.environ.setdefault('DJANGO_SETTINGS_MODULE','onlineshop.settings')

app = Celery('onlineshop')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)