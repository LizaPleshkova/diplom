from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, permissions, viewsets, status, serializers
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from .serializers import MovieListSerializer
from .models import Movie


class MovieView(ListModelMixin, RetrieveModelMixin, CreateModelMixin, viewsets.GenericViewSet,  viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def get_queryset(self, *args, **kwargs):
        # наверное только с текущей даты
        queryset = Movie.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'create':
            return MovieListSerializer
        return MovieListSerializer



