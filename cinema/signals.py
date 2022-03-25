import math
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Hall, Seat


@receiver(post_save, sender=Hall)
def create_seats(sender, instance, created, *args, **kwargs):
    print(instance)
    if created:
        num_seat = 1
        number_of_seats = 10
        columns = math.ceil(number_of_seats / instance.count_rows)
        for i in range(instance.count_rows):
            for j in range(columns):
                if num_seat > number_of_seats:
                    break
                else:
                    new_seat = Seat(
                        hall=instance,
                        number_place=num_seat,
                        number_row=i
                    )
                    new_seat.save()
                    num_seat += 1

        return 'oks'
