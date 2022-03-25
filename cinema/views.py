from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, permissions, viewsets, status, serializers
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import ModelViewSet

from .serializers import CinemaListSerializer, HallListSerializer
from .models import Cinema, Hall


class CinemaView(ModelViewSet):
    permission_classes = (AllowAny,)

    def get_queryset(self, *args, **kwargs):
        # наверное только с текущей даты
        queryset = Cinema.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'create':
            return CinemaListSerializer
        return CinemaListSerializer


class HallView(ModelViewSet):
    permission_classes = (AllowAny,)

    def get_queryset(self, *args, **kwargs):
        queryset = Hall.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'create':
            return HallListSerializer
        return HallListSerializer
