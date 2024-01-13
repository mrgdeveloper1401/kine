from celery import Celery
from datetime import timedelta
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kine.settings')

celery_app = Celery('kine')
celery_app.autodiscover_tasks()

celery_app.conf.broker_url = 'amql://rabitmq'
celery_app.conf.result_backend = 'rpc://'
celery_app.conf.task_serializer = 'json'
celery_app.conf.result_serializer = 'pickle'
celery_app.conf.accept_content = ['pickle', 'json']
celery_app.conf.result_expires = timedelta(minutes=10)
# block client or waiting client
celery_app.conf.task_always_eager = False
celery_app.conf.worker_prefetch_multiplier = 1