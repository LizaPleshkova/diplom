from rest_framework import serializers
from .models import Movie, MovieStudios, Studio


class StudioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ('id', 'name',)


class MovieListSerializer(serializers.ModelSerializer):
    studios = StudioListSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'duration', 'release_date', 'studios', 'genres', 'countries', 'description', 'image',)