from datetime import datetime
import django_filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, permissions, viewsets, status, serializers
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import MovieListSerializer, MovieMainSerializer, MovieRetrieveSerializer
from .models import Movie, Genre
from .services.movie_service import MovieService
from rest_framework.response import Response

from django_filters import rest_framework as filters
from dateutil.parser import parse

class MoviesFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(method='filter_by_genre')
    date = django_filters.CharFilter(method='filter_by_date', label='filter_by_date')
    cinema = django_filters.CharFilter(method='filter_by_cinema', label='cinema')

    class Meta:
        model = Movie
        fields = ['genre', 'date', 'cinema']

    def filter_by_cinema(self, queryset, name, value):
        values = [ int(i) for i in value.split(',')]
        queryset = Movie.objects.filter(session_movie__hall__cinema__id__in=values).distinct()
        return queryset

    def filter_by_genre(self, queryset, name, value):
        print(value)
        values = [ int(i) for i in value.split(',')]
        print(values)
        queryset = Movie.objects.filter(genres__id__in=values).distinct()
        return queryset

    def filter_by_date(self, queryset, name, value):
        print(value)
        values = [ parse(i) for i in value.split(',')]
        queryset = Movie.objects.filter(session_movie__datetime_session__date__in=values)
        return queryset


class MovieView(ListModelMixin, RetrieveModelMixin, CreateModelMixin, viewsets.GenericViewSet, viewsets.ViewSet):
    permission_classes = (AllowAny,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MoviesFilter

    def get_queryset(self, *args, **kwargs):
        # наверное только с текущей даты ScheduleRental.start_date 
        # Movie.objects.filter()
        queryset = Movie.objects.filter(
            movie_rental__end_date__gte=datetime.now()
        )
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return MovieRetrieveSerializer
        return MovieListSerializer

    def retrieve(self, request, *args, **kwargs):
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
        return Response(movies.data, content_type='application/json', status=status.HTTP_200_OK)
  
    @action(methods=['get'], detail=False, url_path='soon')
    def get_movies_soon(self, request):
        movies = MovieService.get_movies_soon()
        movies = MovieMainSerializer(movies, many=True)
        
        return Response(movies.data, content_type='application/json', status=status.HTTP_200_OK)
 
    @action(methods=['get'], detail=False, url_path='latest')
    def get_latest_movies(self, request):
        movies = MovieService.get_latest_movies()
        movies = MovieMainSerializer(movies, many=True)
        return Response(movies.data, content_type='application/json', status=status.HTTP_200_OK)
