from rest_framework import serializers
from .models import Movie, MovieStudios, Studio, Genre, Country


class StudioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ('id', 'name',)


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name',)


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name',)


class MovieListSerializer(serializers.ModelSerializer):
    studios = StudioListSerializer(read_only=True, many=True)
    genres = GenreListSerializer(read_only=True, many=True)
    countries = CountryListSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'duration', 'release_date', 'studios', 'genres', 'countries', 'description', 'image',)
