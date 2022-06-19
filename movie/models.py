from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class PersonalData(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.first_name} - {self.last_name} '

    class Meta:
        verbose_name = "Персональные данные"
        verbose_name_plural ="Персональные данные"



class Studio(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.name} '

    class Meta:
        verbose_name = "Студия"
        verbose_name_plural ="Студии"



class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.name} '

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural ="Страны"



class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.name} '

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural ="Жанры"



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

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural ="Фильмы"



class MovieComposition(models.Model):
    position = models.CharField(max_length=255)
    person = models.ForeignKey('PersonalData', on_delete=models.CASCADE, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.position} - {self.person} - {self.movie} '

    class Meta:
        verbose_name = "Состав фильма"


class MovieCountries(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('movie', 'country'),)


class MovieGenres(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True, related_name='movie_genre')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True, related_name='movie_genre')

    class Meta:
        unique_together = (('movie', 'genre'),)


class MovieStudios(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="ms_movie")
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, related_name='ms_studio')

    class Meta:
        unique_together = (('movie', 'studio'),)


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.author} - {self.movie} - {self.is_visible}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural ="Комментарии"

