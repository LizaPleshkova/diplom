from datetime import datetime
import django_filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from .serializers import (
    MovieListSerializer, MovieMainSerializer, MovieRetrieveSerializer, CommentSerializer, CommentCreateSerializer
)
from .models import Movie, Comment
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
        values = [int(i) for i in value.split(',')]
        queryset = Movie.objects.filter(
            session_movie__datetime_session__gte=datetime.now(),
            session_movie__hall__cinema__id__in=values
        ).distinct()
        return queryset

    def filter_by_genre(self, queryset, name, value):
        values = [int(i) for i in value.split(',')]
        queryset = Movie.objects.filter(
            session_movie__datetime_session__gte=datetime.now(),
            genres__id__in=values
        ).distinct()
        return queryset

    def filter_by_date(self, queryset, name, value):
        values = [parse(i) for i in value.split(',')]
        queryset = Movie.objects.filter(
            session_movie__datetime_session__gte=datetime.now(),
            session_movie__datetime_session__date__in=values
        )
        return queryset


class MovieView(ListModelMixin, RetrieveModelMixin, CreateModelMixin, viewsets.GenericViewSet, viewsets.ViewSet):
    permission_classes = (AllowAny, IsAuthenticatedOrReadOnly)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MoviesFilter

    def get_queryset(self, *args, **kwargs):
        # queryset = Movie.objects.filter(
        #     movie_rental__end_date__gte=datetime.now()
        # )
        # return queryset
        return Movie.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return MovieRetrieveSerializer
        return MovieMainSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        movie_sessions = MovieService.get_sessions_movie(instance.id)
        data = {
            'movie': serializer.data,
            'movie_sessions': movie_sessions
        }
        return Response(data, content_type='application/json', status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='today')
    def get_today_movies(self, request):
        movies_now = MovieService.get_movies_now()
        movies = MovieListSerializer(movies_now, many=True)
        return Response(movies.data, content_type='application/json', status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='current_movies')
    def get_current_movies(self, request):
        ''' use in main page '''
        current_movies = MovieService.get_current_movies()
        movies = MovieMainSerializer(current_movies, many=True)
        return Response(movies.data, content_type='application/json', status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path='comments')
    def comments_movie(self, request, pk=None):
        comments_movie = MovieService.get_comments_movie(pk)
        comments = CommentSerializer(comments_movie, many=True)
        return Response(comments.data, content_type='application/json', status=status.HTTP_200_OK)

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

    @action(methods=['get'], detail=False, url_path='latest')
    def get_latest_movies(self, request):
        movies = MovieService.get_latest_movies()
        movies = MovieMainSerializer(movies, many=True)
        return Response(movies.data, content_type='application/json', status=status.HTTP_200_OK)


class CommentView(ListModelMixin, RetrieveModelMixin, CreateModelMixin, viewsets.GenericViewSet, viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        queryset = Comment.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CommentSerializer
        elif self.action == "create" or self.action == "post":
            return CommentCreateSerializer
        return CommentSerializer

    def create(self, request, *args, **kwargs):
        comment_data = self.request.data
        comment_data['author'] = self.request.user.id
        serializer = self.get_serializer(data=comment_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
