from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from movie.models import Movie


class Cinema(models.Model):
    id_cinema = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField("Изображение", upload_to="cinemas/", blank=True, null=True)

    def __str__(self):
        return f'{self.id_cinema} - {self.name} - {self.address}- {self.phone_number}'

    def get_absolute_url(self):
        return reverse('cinema_detail', kwargs={"slug": self.name})


class Hall(models.Model):
    # delete count rows
    # validate count places <10
    id_hall = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    id_cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE,) # cinema
    count_places = models.IntegerField()
    count_rows = models.IntegerField()
    count_columns = models.IntegerField()

    def __str__(self):
        return f'{self.id_hall} - {self.name} - {self.id_cinema} - {self.count_places} '


class Sector(models.Model):
    id_sector = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.id_sector} - {self.name}'


class Seat(models.Model):
    # boolean field sit or not
    id_seat = models.AutoField(primary_key=True) #del
    id_hall = models.ForeignKey(Hall, models.DO_NOTHING) # hall? cascade
    id_sector = models.ForeignKey(Sector, models.DO_NOTHING, blank=True, null=True)# sector cascade
    number_place = models.IntegerField()
    number_row = models.IntegerField() #ddel

    def __str__(self):
        return f'{self.id_seat} - {self.id_hall} - {self.id_sector} - {self.number_place} - {self.number_row} '


class ScheduleRental(models.Model):
    '''  прокат фильма '''
    id_rental = models.AutoField(primary_key=True) # del
    id_movie = models.ForeignKey(Movie, models.DO_NOTHING, related_name='movie_rental') # on_del
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.id_rental} - {self.id_movie} - [{self.start_date} - {self.end_date}] '


class SessionSchedule(models.Model):
    ''' '''
    id_session = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = (('start_time', 'end_time'),)

    def __str__(self):
        return f'{self.id_session} - {self.name} - {self.start_time} - {self.end_time} '


class MovieSession(models.Model):
    ''' киноcеанс '''
    id_session = models.AutoField(primary_key=True)
    id_hall = models.ForeignKey(Hall, models.DO_NOTHING, blank=True, null=True)#
    id_movie = models.ForeignKey(Movie, models.DO_NOTHING, blank=True, null=True)#
    datetime_session = models.DateTimeField()

    def __str__(self):
        return f'{self.id_session} - {self.id_hall} - {self.id_movie} - {self.datetime_session} '

