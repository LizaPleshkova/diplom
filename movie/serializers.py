from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Movie, MovieStudios, Studio, Genre, Country, Comment
from client.serializers import UserListSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    author = UserListSerializer()

    # author = serializers.CharField(source="author.username")

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'movie', 'date', 'is_visible')
        # fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print('in repr', representation)
        user = representation['author']
        representation['author'] = {
            "id": user['id'], "username": user['username']
        }
        return representation


class CommentCreateSerializer(serializers.ModelSerializer):
    # author = UserListSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'movie')
        # fields = '__all__'

    def to_internal_value(self, data):
        representation = super().to_internal_value(data)
        print('in repr', representation)
        user = representation['author']
        # u = User.objects.get()
        # user = get_object_or_404(User, id=representation['author'])
        # user = get_object_or_404(User, id=representation['author'])
        representation['author'] = user

        return representation


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

    # start_date = serializers.DateField()
    class Meta:
        model = Movie
        fields = ('id', 'name', 'duration', 'release_date', 'studios', 'genres', 'countries', 'description', 'image',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['genres'] = [j['name'] for j in representation['genres']]
        representation['studios'] = [j['name'] for j in representation['studios']]
        representation['countries'] = [j['name'] for j in representation['countries']]
        url = "http://127.0.0.1:8000/media/movies/EYjhfIcdATk.jpg"
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
