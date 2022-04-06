import django_filters
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, permissions, viewsets, status, serializers
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import MovieListSerializer, MovieRetrieveSerializer
from .models import Movie, Genre
from .services.movie_service import MovieService
from rest_framework.response import Response

from django_filters import rest_framework as filters


class MoviesFilter(django_filters.FilterSet):
    # genres = django_filters.CharFilter(field_name='genres__name')
    # genres = django_filters.NumberFilter(field_name="genres")
    genres = django_filters.AllValuesFilter
    # genre = django_filters.CharFilter(method='filter_by_genre')
    date = django_filters.CharFilter(method='filter_by_date', label='filter_by_date')
    cinema = django_filters.CharFilter(method='filter_by_cinema', label='cinema')

    class Meta:
        model = Movie
        fields = ['genres', 'date', 'cinema']

    def filter_by_cinema(self, queryset, name, value):
        queryset = Movie.objects.filter(Q(session_movie__hall__cinema__name=value))
        return queryset

    def filter_by_genre(self, queryset, name, value):
        print(value)
        queryset = Movie.objects.filter(Q(genres__name=value))
        return queryset

    def filter_by_date(self, queryset, name, value):
        print(value)
        queryset = Movie.objects.filter(Q(session_movie__datetime_session__date=value))
        return queryset


#


class MovieView(ListModelMixin, RetrieveModelMixin, CreateModelMixin, viewsets.GenericViewSet, viewsets.ViewSet):
    permission_classes = (AllowAny,)
    filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('genres__name',)
    filterset_class = MoviesFilter

    def get_queryset(self, *args, **kwargs):
        # наверное только с текущей даты ScheduleRental.start_date 
        # Movie.objects.filter()
        queryset = Movie.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return MovieRetrieveSerializer
        return MovieListSerializer

    def retrieve(self, request, *args, **kwargs):
        ''' рассортировать киносеансы по киинотеарам '''
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        movie_sessions = MovieService.get_sessions_movie(instance.id)
        print(movie_sessions)
        data = {
            'movie': serializer.data,
            'movie_sessions': movie_sessions
        }
        return Response(data, content_type='application/json', status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='now')
    def movies_now(self, request):
        movies_now = MovieService.get_movies_now()
        movies = MovieListSerializer(movies_now, many=True)
        # nb = json.dumps(m.data)
        return Response(movies.data, content_type='application/json', status=status.HTTP_200_OK)
