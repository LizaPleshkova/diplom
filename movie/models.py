from django.db import models
from django.urls import reverse


class PersonalData(models.Model):
    id_person = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id_person} - {self.first_name} - {self.last_name} '


class Studio(models.Model):
    id_studio = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id_studio} - {self.name} '


class Country(models.Model):
    id_country = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id_country} - {self.name} '


class Genre(models.Model):
    id_genre = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id_genre} - {self.name} '


class Movie(models.Model):
    id_movie = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    duration = models.TimeField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True, related_name='movie_genres')
    countries = models.ManyToManyField(Country, blank=True, related_name='movie_countries')
    studios = models.ManyToManyField(Studio, blank=True, related_name='movie_studios')
    category = models.IntegerField(blank=True, null=True)
    image = models.ImageField("Изображение", upload_to="movies/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.id_movie} - {self.name} '

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={"pk": self.id_movie})


class MovieComposition(models.Model):
    position = models.CharField(max_length=255)
    id_person = models.ForeignKey('PersonalData', models.DO_NOTHING, blank=True, null=True)
    id_movie = models.ForeignKey(Movie, models.DO_NOTHING)

    def __str__(self):
        return f'{self.position} - {self.id_person} - {self.id_movie} '


class MovieCountries(models.Model):
    id = models.BigAutoField(primary_key=True)
    movie = models.ForeignKey(Movie, models.DO_NOTHING)
    country = models.ForeignKey(Country, models.DO_NOTHING)

    class Meta:
        unique_together = (('movie', 'country'),)


class MovieGenres(models.Model):
    id = models.BigAutoField(primary_key=True)
    movie = models.ForeignKey(Movie, models.DO_NOTHING, related_name='movie_genre')
    genre = models.ForeignKey(Genre, models.DO_NOTHING, related_name='m_genre')

    class Meta:
        unique_together = (('movie', 'genre'),)


class MovieStudios(models.Model):
    id = models.BigAutoField(primary_key=True)
    movie = models.ForeignKey(Movie, models.DO_NOTHING)
    studio = models.ForeignKey('Studio', models.DO_NOTHING)

    class Meta:
        unique_together = (('movie', 'studio'),)
