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

class MovieMainSerializer(serializers.ModelSerializer):
    studios = StudioListSerializer(read_only=True, many=True)
    genres = GenreListSerializer(read_only=True, many=True)
    countries = CountryListSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'duration', 'release_date', 'studios', 'genres', 'countries', 'description', 'image',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['genres'] = [ j['name']for j in representation['genres']]
        representation['studios'] = [ j['name']for j in representation['studios']]
        representation['countries'] = [ j['name']for j in representation['countries']]
        url ="http://127.0.0.1:8000/media/movies/EYjhfIcdATk.jpg"
        if "http://127.0.0.1:8000/" not in representation['image']:
            representation['image'] = "http://127.0.0.1:8000" + representation['image']
        
        return representation

class MovieRetrieveSerializer(serializers.ModelSerializer):
    ''' add actors '''
    studios = StudioListSerializer(read_only=True, many=True)
    genres = GenreListSerializer(read_only=True, many=True)
    countries = CountryListSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = (
            'id', 'name', 'duration', 'release_date', 'studios', 'genres',
            'countries', 'description', 'image',
        )
