from django.core.management.base import BaseCommand
from accounts.models import OtpCode
from datetime import datetime, timedelta
import pytz


class Command(BaseCommand):
    help = 'Remove OTP code expired'

    def handle(self, *args, **options):
        expire = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
        OtpCode.objects.filter(create_at__lt=expire).delete()
        self.stdout.write('all expired otp code removed')
