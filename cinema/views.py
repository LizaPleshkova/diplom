import json
from datetime import datetime, timedelta
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, status, serializers
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import CinemaListSerializer, HallListSerializer, HallCreateSerializer, SeatIdSerializer, SeatListSerializer, \
    BookingSerializer, MovieSessionSerializer
from .models import Cinema, Hall, MovieSession, Booking, Seat, BookingHistory, ActionChoice
from .services.BookingService import BookingClassService

from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie.models import Genre
from movie.serializers import GenreListSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


def _get_range_dates():
    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=5)

    # start = datetime.strptime(start_date, '%A, %d %B %Y')
    start = datetime.strptime(str(start_date), '%Y-%m-%d')
    end = datetime.strptime(str(end_date), '%Y-%m-%d')

    daterange = [(start + timedelta(days=x)).strftime('%Y-%m-%d') for x in range(0, (end - start).days)]
    print(daterange)
    return daterange


@api_view(['GET'])
def filters_data(request):
    # latest = MovieService.get_latest_movies()

    genres = Genre.objects.all()
    dates = _get_range_dates()
    cinema_list = Cinema.objects.all()

    filters_data = {
        'dates': dates,
        'cinemas': CinemaListSerializer(cinema_list, many=True).data,
        'genres': GenreListSerializer(genres, many=True).data,
    }
    return Response(filters_data, content_type='application/json', status=status.HTTP_200_OK)


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

    @action(methods=['get'], detail=False, url_path='update-booking', url_name='update_booking')
    def update_booking_seats(self, request, pk=None):
        movie_session_time = MovieSession.objects.filter(datetime_session__lte=datetime.now())
        for ms in movie_session_time:
            # все забронированные места в выбранных киносеансах
            booking_ms = Booking.objects.filter(
                session=ms
            )
            for booking in booking_ms:
                booking_history = BookingHistory.objects.create(
                    action=ActionChoice.DELETE.value,
                    user=booking.user,
                    session=booking.session,
                    seat=booking.seat,
                    price=booking.price,
                    datetime_book=booking.datetime_book
                )
                booking_history.save()
                print(' for del ', booking)
                booking.delete()

        return Response(content_type="application/json", status=status.HTTP_200_OK)


class MovieSessionView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = MovieSessionSerializer

    def get_queryset(self):
        queryset = MovieSession.objects.filter(datetime_session__date__gte=datetime.now().date())
        return queryset
    
    @action(methods=['get'], detail=True, url_path='get-seats', url_name='get_seats')
    def get_seats(self, request, pk=None):
        # movie_session_id = self.get_object()
        free_seats, booked_seats = BookingClassService.get_free_booked_seats(pk)
        seats = {
            'count_free_seats': free_seats.count(),
            'count_booked_seats': booked_seats.count(),
            'free_seats': SeatListSerializer(free_seats, many=True).data,
            'booked_seats': SeatListSerializer(booked_seats, many=True).data
        }
        return Response(seats, content_type="application/json", status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path='seats', url_name='seats')
    def get_seats_layout(self, request, pk=None):
        # movie_session_id = self.get_object()
        free_seats, booked_seats = BookingClassService.get_free_booked_seats(pk)

        movie_session = MovieSession.objects.get(id=pk)
        # нужно получить зал и все места в нем
        seats = Seat.objects.select_related('sector').filter(
            hall=movie_session.hall
        ).order_by('number_place')
        seat_layot = BookingClassService.create_seat_layout(seats, pk)
        print(seat_layot)
        seats = {
            'seat_layout':seat_layot,
            'count_free_seats': free_seats.count(),
            'movie_session': MovieSessionSerializer(movie_session).data,
            'free_seats': SeatListSerializer(free_seats, many=True).data,
            'booked_seats': booked_seats
        }
        return Response(seats, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='booking', url_name='booking')
    def booking_seats(self, request, pk=None):
        #
        # user = User.objects.get(username='admin')
        # self.requestuser = user
        # print(self.request.user)
        booking_instance = BookingClassService.create_booking(pk, request)
        if booking_instance:
            return Response(booking_instance, content_type="application/json", status=status.HTTP_201_CREATED)
        else:
            return Response(content_type="application/json", status=status.HTTP_400_BAD_REQUEST)
