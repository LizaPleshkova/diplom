import django_filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, permissions, viewsets, status, serializers
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import MovieListSerializer
from .models import Movie, Genre
from .services.movie_service import MovieService
from ..cinema.models import Cinema
from ..cinema.services import Service


class FilterMoviesView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['user', 'is_active']

    def get_queryset(self):
        cinemas = Cinema.objecys.all()
        dates = Service.get_range_dates()
        genres = Genre.objects.all()
        return cinemas + dates + genres

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class MovieView(ListModelMixin, RetrieveModelMixin, CreateModelMixin, viewsets.GenericViewSet, viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def get_queryset(self, *args, **kwargs):
        # наверное только с текущей даты ScheduleRental.start_date 
        # Movie.objects.filter()
        queryset = Movie.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'create':
            return MovieListSerializer
        return MovieListSerializer

    @action(methods=['get'], detail=False, url_path='now')
    def movies_now(self, request):
        movies_now = MovieService.get_movies_now()
        movies = MovieListSerializer(movies_now, many=True)
        # nb = json.dumps(m.data)
        return Response(movies.data, content_type='application/json', status=status.HTTP_200_OK)
