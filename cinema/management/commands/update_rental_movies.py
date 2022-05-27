from datetime import datetime

from django.core.management.base import BaseCommand, CommandError

from ...models import Sector, MovieSession,  ScheduleRental


class Command(BaseCommand):

    def handle(self, *args, **options):
        ms = ScheduleRental.objects.all()
        for i in ms:
            i.start_date = datetime(2021, 10, 10)
            i.end_date = datetime(2021, 12, 16)
        ScheduleRental.objects.bulk_update(ms, ['start_date', 'end_date'])
