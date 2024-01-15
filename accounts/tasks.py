from celery import shared_task
from datetime import datetime, timedelta
import pytz
from .models import OtpCode


@shared_task()
def remove_expire_code():
    expire = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
    OtpCode.objects.filter(create_at__lt=expire).delete()
