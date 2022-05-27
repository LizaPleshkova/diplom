from datetime import datetime

from django.core.management.base import BaseCommand, CommandError

from ...models import Sector, MovieSession


class Command(BaseCommand):

    def handle(self, *args, **options):
        ms = MovieSession.objects.all()
        for i in ms:
            i.datetime_session = datetime.now()
        MovieSession.objects.bulk_update(ms, ['datetime_session'])
        #
        # tickets = Ticket.objects.all()
        # for i in tickets:
        #     i.datetime_order = datetime.now()
        # Ticket.objects.bulk_update(tickets, ['datetime_order'])
