import json
from datetime import datetime
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, status, serializers
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import CinemaListSerializer, HallListSerializer, HallCreateSerializer, SeatListSerializer, \
    BookingSerializer
from .models import Cinema, Hall, MovieSession, Booking, Seat
from .services.BookingService import BookingClassService


class BookingView(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CinemaListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Booking.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'create':
            return CinemaListSerializer
        return CinemaListSerializer


class CinemaView(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CinemaListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Cinema.objects.all()
        return queryset


class HallView(ModelViewSet):
    permission_classes = (AllowAny,)

    def get_queryset(self, *args, **kwargs):
        queryset = Hall.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'create':
            return HallCreateSerializer
        return HallListSerializer


class SeatView(ListModelMixin, RetrieveModelMixin, CreateModelMixin, viewsets.GenericViewSet, viewsets.ViewSet):
    permission_classes = (AllowAny,)
    serializer_class = HallListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Hall.objects.all()
        return queryset


class BookingView(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet, viewsets.ViewSet):
    permission_classes = (AllowAny,)
    serializer_class = BookingSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Booking.objects.all()
        return queryset


class MovieSessionView(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = BookingSerializer

    def get_queryset(self):
        queryset = MovieSession.objects.filter(datetime_session__date__gte=datetime.now().date())
        return queryset

    @action(methods=['get'], detail=False, url_path='(?P<pk>[^/.]+)/get-seats', url_name='get-seats')
    def get_seats(self, request, **kwargs):
        movie_session_id = kwargs.get('pk')
        free_seats, booked_seats = BookingClassService.get_free_booked_seats(movie_session_id)
        seats = {
            'count_free_seats': free_seats.count(),
            'count_booked_seats': booked_seats.count(),
            'free_seats': SeatListSerializer(free_seats, many=True).data,
            'booked_seats': SeatListSerializer(booked_seats, many=True).data
        }
        return Response(seats, content_type="application/json", status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='(?P<pk>[^/.]+)/booking', url_name='booking')
    def booking_seats(self, request, **kwargs):
        movie_session_id = kwargs.get('pk')

        booking_instance = BookingClassService.create_booking(movie_session_id, request)
        if booking_instance:
            return Response(booking_instance, content_type="application/json", status=status.HTTP_200_OK)
        else:
            return Response(content_type="application/json", status=status.HTTP_400_BAD_REQUEST)
