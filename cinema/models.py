import math
from enum import Enum
import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db import models
from movie.models import Movie

User = get_user_model()

COUNT_COLLUMNS_HALL = 3


class SectorChoice(Enum):
    VIP = 'VIP'
    A = 'A'
    B = 'B'
    C = 'C'


class Cinema(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(
        "Изображение", upload_to="cinemas/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Кинотеатр"
        verbose_name_plural = "Кинотеатры"

    def __str__(self):
        # return f'{self.pk} - {self.name} - {self.address}- {self.phone_number}'
        return f'[{self.pk} - {self.name} - {self.address}]'

    def get_absolute_url(self):
        return reverse('cinema_detail', kwargs={"slug": self.name})


class Hall(models.Model):
    '''  validate count places <10 '''
    name = models.CharField(max_length=100, verbose_name="Название зала")
    cinema = models.ForeignKey(
        Cinema, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Кинотеатр")
    count_places = models.IntegerField(verbose_name="Количество мест")
    count_rows = models.IntegerField(default=0, verbose_name="Количество рядов")
    count_columns = models.IntegerField(default=0, verbose_name="Количество колон")

    def hall_cinema(self):
        return f'{self.cinema.id}-{self.cinema.name}'

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"

    def __str__(self):
        return f'{self.pk} - {self.name} - {self.cinema}- {self.count_places}'


class Sector(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Сектор"
        verbose_name_plural = "Сектора"

    def __str__(self):
        return f'{self.pk} - {self.name}'


class Seat(models.Model):
    '''  boolean field sit or not '''
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    sector = models.ForeignKey(
        Sector, on_delete=models.DO_NOTHING, blank=True, null=True)
    number_place = models.IntegerField()
    number_row = models.IntegerField(default=0)
    isBooked = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return f'{self.pk} - {self.hall} -{self.isBooked}- {self.sector} - {self.number_place}'


class ScheduleRental(models.Model):
    '''  прокат фильма '''
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True,
                              related_name='movie_rental')  # not on_delte
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = "Прокат фильма"

    def __str__(self):
        return f'{self.pk} - {self.movie} - [{self.start_date} - {self.end_date}] '


class SessionSchedule(models.Model):
    ''' example:
     morning session: 9am - 12 am
     afternonon session: 12am - 4 pm
     evening sesssion: 5pm - 8 pm
    '''
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = (('start_time', 'end_time'),)
        verbose_name = "Расписание киносеанса"
        verbose_name_plural = "Расписание киносеансов"

    def __str__(self):
        return f'{self.pk} - {self.name} - {self.start_time} - {self.end_time} '


class MovieSession(models.Model):
    ''' киноcеанс '''
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE,
                             blank=True, null=True, related_name='session_hall', verbose_name="Зал")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              blank=True, null=True, related_name='session_movie', verbose_name="Фильм")
    datetime_session = models.DateTimeField(verbose_name="Время киносеанса")

    class Meta:
        verbose_name = "Киносеанс"
        verbose_name_plural = "Киносеансы"

    def __str__(self):
        return f'{self.pk} - {self.hall} - {self.movie}'


class Booking(models.Model):
    id_ticket = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(
        MovieSession,
        on_delete=models.CASCADE,
        related_name='booking_ms'
    )
    seat = models.ForeignKey(
        Seat, on_delete=models.CASCADE, related_name='booking_seat')
    price = models.DecimalField(
        max_digits=1000, decimal_places=2, blank=True, null=True)
    datetime_book = models.DateTimeField()
    isPaid = models.BooleanField(default=False)

    class Meta:
        unique_together = (('session', 'seat'),)
        verbose_name = "Бронь"
        verbose_name_plural = "Бронирования"

    def __str__(self):
        return f'{self.id} - {self.user.username} - {self.session} - {self.seat.number_place} - {self.price} - {self.datetime_book} '


class ActionChoice(Enum):
    DELETE = 'Delete'
    CREATE = 'Create'
    UPDATE = 'Update'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class BookingHistory(models.Model):
    '''
    может добавить что именно сделал пользователь: удалил\добавил
    => signal ( after save Booking)
    '''
    action = models.CharField(
        "Type of action", max_length=7, choices=ActionChoice.choices(), null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(
        MovieSession,
        on_delete=models.CASCADE,
        related_name='history_ms'
    )
    seat = models.ForeignKey(
        Seat, on_delete=models.CASCADE, related_name='history_seat')
    price = models.DecimalField(
        max_digits=1000, decimal_places=2, blank=True, null=True)
    datetime_book = models.DateTimeField()
    action_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "История бронирования"
        verbose_name_plural = "История броинирования"


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
                        number_row=row,
                        isBooked=False
                    )
                    print(new_seat)
                    new_seat.save()
                    num_seat += 1
    else:
        print('not run')
