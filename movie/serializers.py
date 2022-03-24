from rest_framework import serializers
from .models import Movie, MovieStudios, Studio

# question about many-to-many fields
# through studios = StudioslListSerializer(read_only=True, many=True) or to_representation()

class StudioListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Studio
        fields = ('name')


class StudioslListSerializer(serializers.ModelSerializer):
    studio = StudioListSerializer(read_only=True, many=True)

    class Meta:
        model = MovieStudios
        fields = ('studio')


class MovieListSerializer(serializers.ModelSerializer):
    # studios = StudioslListSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'duration', 'release_date', 'studios', 'genres', 'countries', 'description', 'image')

    def to_representation(self, data):
        representation = super().to_representation(data)

        id = representation['id']
        studios = Studio.objects.filter(movie_studios__id=id).values()
        print(studios)
        representation['studios'] = studios
        return representation




