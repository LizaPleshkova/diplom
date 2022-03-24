from django.db import models
from django.urls import reverse


class PersonalData(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.first_name} - {self.last_name} '


class Studio(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.name} '


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.name} '


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.name} '


class Movie(models.Model):
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
        return f'{self.id} - {self.name} '

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={"id": self.id})


class MovieComposition(models.Model):
    position = models.CharField(max_length=255)
    person = models.ForeignKey('PersonalData', on_delete=models.CASCADE, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.position} - {self.person} - {self.movie} '


class MovieCountries(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('movie', 'country'),)


class MovieGenres(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,blank=True, null=True,  related_name='movie_genre')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True, related_name='movie_genre')

    class Meta:
        unique_together = (('movie', 'genre'),)


class MovieStudios(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="ms_movie")
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, related_name='ms_studio')

    class Meta:
        unique_together = (('movie', 'studio'),)
