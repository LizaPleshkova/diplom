import math
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Hall, Seat, Sector, SectorChoice


@receiver(post_save, sender=Hall)
def create_seats(sender, instance, created, *args, **kwargs):
    if created:
        print(instance)
        number_of_seats = instance.count_places
        num_seat = 1
        count_rows = 3  # or 4

        sector_A = Sector.objects.get(name=SectorChoice.A.value)
        sector_C = Sector.objects.get(name=SectorChoice.C.value)
        sector_B = Sector.objects.get(name=SectorChoice.B.value)

        columns = math.ceil(number_of_seats / count_rows)
        for row in range(count_rows):
            for column in range(columns):
                if num_seat > number_of_seats:
                    break
                else:
                    if row == 0:
                        sector = sector_A
                    elif row == 1:
                        sector = sector_B
                    else:
                        sector = sector_C
                    new_seat = Seat(
                        hall=instance,
                        number_place=num_seat,
                        sector=sector,
                        number_row=row
                    )
                    print(new_seat)
                    new_seat.save()
                    num_seat += 1
    else:
        print('not run')
