from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from movie.models import Movie


class Cinema(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField("Изображение", upload_to="cinemas/", blank=True, null=True)

    def __str__(self):
        return f'{self.pk} - {self.name} - {self.address}- {self.phone_number}'

    def get_absolute_url(self):
        return reverse('cinema_detail', kwargs={"slug": self.name})


class Hall(models.Model):
    '''  validate count places <10 '''
    name = models.CharField(max_length=100)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, blank=True, null=True)
    count_places = models.IntegerField()

    def __str__(self):
        return f'{self.pk} - {self.name} - {self.cinema}- {self.count_places}'


class Sector(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.pk} - {self.name}'


class Seat(models.Model):
    '''  boolean field sit or not '''
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.DO_NOTHING, blank=True, null=True)
    number_place = models.IntegerField()

    def __str__(self):
        return f'{self.pk} - {self.hall} - {self.sector} - {self.number_place}'


class ScheduleRental(models.Model):
    '''  прокат фильма '''
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True,
                              related_name='movie_rental')  # not on_delte
    start_date = models.DateField()
    end_date = models.DateField()

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

    def __str__(self):
        return f'{self.pk} - {self.name} - {self.start_time} - {self.end_time} '


class MovieSession(models.Model):
    ''' киноcеанс '''
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, blank=True, null=True, related_name='session_hall')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True, related_name='session_movie')
    datetime_session = models.DateTimeField()

    def __str__(self):
        return f'{self.pk} - {self.hall} - {self.movie}'
