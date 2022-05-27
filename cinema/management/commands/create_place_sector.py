import math
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError

from ...models import Seat, Sector, Hall


class Command(BaseCommand):

    def handle(self, *args, **options):
        instance = Hall.objects.get(id_hall=6)
        sector_A = Sector.objects.get(id_sector=7)
        sector_C = Sector.objects.get(id_sector=8)
        print(instance)
        number_of_seats = instance.count_places
        num_seat = 1
        columns = math.ceil(number_of_seats / instance.count_rows)
        for i in range(instance.count_rows):
            for j in range(columns):
                if num_seat > number_of_seats:
                    break
                else:
                    if (i==2 and j ==2) or (i==3 and j==2):
                        sector = sector_A
                    else:
                        sector = sector_C
                    new_seat = Seat(
                        id_hall=instance,
                        number_place=num_seat,
                        id_sector=sector,
                        number_row=i
                    )
                    new_seat.save()
                    num_seat += 1

        return 'oks'
