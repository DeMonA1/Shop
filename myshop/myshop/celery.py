import os
from celery import Celery


# set the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app: Celery = Celery('myshop')
# use CELERY_ prefix for all Celery settings in settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')
# Celery looks for all tasts.py files into app direcories, which included into INSTALLED_APPS
app.autodiscover_tasks()

