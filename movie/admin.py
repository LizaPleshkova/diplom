from django.contrib import admin
from .models import (
    Country, Genre, Movie, MovieComposition, PersonalData, Studio
)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']


class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name','duration', 'release_date', 'category',
        # 'id_movie', 'name', 'genres', 'countries', 'studios', 'duration', 'release_date', 'category',
    )
    list_filter = ['genres', 'countries', 'studios', 'category']
    # list_filter = ['genres', 'countries', 'studios', 'category']
    search_fields = ['name']


class MovieCompositionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'position', 'person', 'movie',
    )
    list_filter = ['position', 'person', 'movie']
    search_fields = ['position']


class PersonalDataCompositionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name',
    )
    search_fields = ['first_name']


class StudioAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name'
    )
    search_fields = ['name']


admin.site.register(Country, CountryAdmin)

admin.site.register(Genre, GenreAdmin)

admin.site.register(Movie, MovieAdmin)

admin.site.register(MovieComposition, MovieCompositionAdmin)

admin.site.register(PersonalData, PersonalDataCompositionAdmin)

admin.site.register(Studio, StudioAdmin)
