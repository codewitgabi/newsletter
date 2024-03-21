import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Newsletter.settings')

celery_app = Celery("Newsletter", broker="amqp://", backend="rpc://")

celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    "send-weekly-updates": {
        "task": "send_weeky_updates",
        "schedule": crontab(minute=0, hour=8, day_of_week=6) # cron job to send weekly updates every saturday at 8am
    },
}
