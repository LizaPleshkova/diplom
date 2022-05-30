from datetime import datetime, timedelta
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import ModelViewSet
from cinema.services.Service import CinemaService
from .serializers import (
    CinemaListSerializer, HallListSerializer, HallCreateSerializer, MovieSessionMainSerializer,
    SeatListSerializer, BookingSerializer
)
from .models import Cinema, Hall, MovieSession, Booking, Seat
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

    start = datetime.strptime(str(start_date), '%Y-%m-%d')
    end = datetime.strptime(str(end_date), '%Y-%m-%d')

    daterange = [(start + timedelta(days=x)).strftime('%Y-%m-%d') for x in range(0, (end - start).days)]
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


class CinemaView(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CinemaListSerializer

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return CinemaListSerializer
    #     return CinemaListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Cinema.objects.all()
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        ms = CinemaService.get_cinema_sessions(instance.id)
        ser = MovieSessionMainSerializer(ms, many=True)
        return Response({'cinema': serializer.data, 'movie_session': ser.data})

    @action(methods=['get'], detail=True, url_path='movie-session', url_name='movie_session')
    def get_movie_session(self, request, pk=None):
        ms = CinemaService.get_cinema_sessions(pk)
        ser = MovieSessionMainSerializer(ms, many=True)
        return Response(ser.data, content_type="application/json", status=status.HTTP_200_OK)


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

    @action(methods=['get'], detail=False, url_path='update-seats', url_name='update_seats')
    def update_seats_status(self, request):
        seats = Seat.objects.all()
        for seat in seats:
            seat.isBooked = False
            seat.save(update_fields=["isBooked"])
        return Response(content_type="application/json", status=status.HTTP_200_OK)


class BookingView(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet, viewsets.ViewSet):
    permission_classes = (AllowAny,)
    serializer_class = BookingSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Booking.objects.all()
        return queryset

    def delete(self, request, pk):
        booking = self.get_object()
        print(booking)
        BookingClassService.delete_booking(booking)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=False, url_path='update-booking', url_name='update_booking')
    def update_booking_seats(self, request, pk=None):
        BookingClassService.update_all_booking()
        # movie_session_time = MovieSession.objects.filter(datetime_session__lte=datetime.now())

        # movie_session_time = MovieSession.objects.get(id=int(pk))
        # print(movie_session_time)
        # seats = Seat.objects.filter(
        #     hall=movie_session_time.hall
        # ).update(isBooked=False)
        # print(seats)
        #
        # booking_ms = Booking.objects.filter(
        #     session=movie_session_time
        # )
        # for booking in booking_ms:
        #     booking_history = BookingHistory.objects.create(
        #         action=ActionChoice.DELETE.value,
        #         user=booking.user,
        #         session=booking.session,
        #         seat=booking.seat,
        #         price=booking.price,
        #         datetime_book=booking.datetime_book
        #     )
        #     booking.seat.isBooked = True
        #     booking.seat.save(update_fields=["isBooked"])
        #     booking_history.save()
        #     print(' for del ', booking)
        #     booking.delete()

        return Response(content_type="application/json", status=status.HTTP_200_OK)


class MovieSessionView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = MovieSessionMainSerializer

    def get_queryset(self):
        queryset = MovieSession.objects.filter(datetime_session__date__gte=datetime.now().date())
        return queryset

    @action(methods=['get'], detail=True, url_path='get-seats', url_name='get_seats')
    def get_seats(self, request, pk=None):
        # BookingClassService.update_all_booking()

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
        # free_seats, booked_seats = BookingClassService.get_free_booked_seats(pk)

        movie_session = MovieSession.objects.get(id=pk)
        # нужно получить зал и все места в нем
        seats = Seat.objects.select_related('sector').filter(
            hall=movie_session.hall
        ).order_by('number_place')
        seat_layot = BookingClassService.create_seat_layout(seats, pk)
        seats = {
            'seat_layout': seat_layot,
            'count_free_seats': seats.filter(isBooked=False).count(),
            'movie_session': MovieSessionMainSerializer(movie_session).data,
        }
        return Response(seats, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='booking', url_name='booking')
    def booking_seats(self, request, pk=None):
        try:
            print(pk, type(pk))
            booking_instance = BookingClassService.create_booking(int(pk), request)
            if booking_instance:
                print('CREATE BOOKING INST', booking_instance)
                return Response(booking_instance, content_type="application/json", status=status.HTTP_201_CREATED)
            else:
                print('smth worong')
        except BaseException as error:
            print('An exception occurred: {}'.format(error))
            return Response(format(error), content_type="application/json", status=status.HTTP_400_BAD_REQUEST)
