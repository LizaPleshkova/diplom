import math
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from ...models import Seat, Sector, Hall, SectorChoice


class Command(BaseCommand):
    help = 'Create places in hall'

    def add_arguments(self, parser):
        parser.add_argument('id_hall', type=int, help='id hall where create places')

    def handle(self, *args, **options):
        id_hall = options['id_hall']
        hall = Hall.objects.get(id=id_hall)  # 14
        sector_A = Sector.objects.get(name=SectorChoice.A.value)
        sector_C = Sector.objects.get(name=SectorChoice.C.value)
        sector_B = Sector.objects.get(name=SectorChoice.B.value)

        print(hall)
        number_of_seats = hall.count_places
        count_rows = 3  # or 4
        num_seat = 1
        columns = math.ceil(number_of_seats / count_rows)
        for i in range(count_rows):
            for j in range(columns):
                if num_seat > number_of_seats:
                    break
                else:
                    print("num_seat", num_seat)
                    if (i == 0 and (j == 0 or j == 2)) or (i == 1 and (j == 0 or j == 2)):
                        sector = sector_A
                    elif ((i == 0 or i == 1) and j == 1):
                        sector = sector_B
                    else:
                        sector = sector_C
                    new_seat = Seat(
                        hall=hall,
                        number_place=num_seat,
                        sector=sector,
                        number_row=i
                    )
                    new_seat.save()
                    num_seat += 1

        return 'done'
