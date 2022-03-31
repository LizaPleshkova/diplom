import base64
import json
from datetime import datetime, date
from turtle import pd
import holidays
from ..models import Booking, Seat, MovieSession, SectorChoice
from django.contrib.auth import get_user_model

from ..serializers import BookingSerializer

User = get_user_model()


def _get_user_id_from_token(request):
    token = http_auth = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace("Token ", "")
    user_json = json.loads(base64.b64decode(token.split(".")[1]))
    print(user_json)
    return user_json['user_id']


def _get_free_booked_seats(pk_session: int):
    # get id of booked_seats in the movie_session
    booked_seats = Booking.objects.filter(session=pk_session)

    # get id of booked_seats(Seat model)
    ids_booked_seats = [bs.seat.id for bs in booked_seats]

    hall = MovieSession.objects.get(id=pk_session).hall

    free_seats = Seat.objects.filter(hall__id=hall.id).exclude(id__in=ids_booked_seats)
    booked_seats = Seat.objects.filter(id__in=ids_booked_seats)
    return free_seats, booked_seats


class BookingClassService:

    @staticmethod
    def create_booking(session_id: int, request):
        user_id = _get_user_id_from_token(request)
        booking_instance = request.data.dict()
        booking_instance['user'] = user_id

        if 'session' not in booking_instance:
            booking_instance['session'] = session_id

        ser = BookingSerializer(
            data=booking_instance,
            context={'user': User.objects.get(id=user_id), 'session': session_id}
        )
        if ser.is_valid(raise_exception=True):
            instance = ser.save()
            return ser.data


    @staticmethod
    def get_ids_booked_seats(pk_session: int):
        booked_seats = Booking.objects.filter(session=pk_session)
        booked_seats_list = [seat.seat.number_place for seat in booked_seats]
        return booked_seats_list

    @staticmethod
    def get_free_seats(pk_session: int):
        booked_seats = Booking.objects.filter(session=pk_session)
        ms_hall = MovieSession.objects.filter(id=pk_session).hall
        free_seats = Seat.objects.filter(hall=ms_hall)

    @staticmethod
    def get_free_booked_seats(pk_session: int) -> object:
        # get id of booked_seats in the movie_session
        booked_seats = Booking.objects.filter(session=pk_session)

        # get id of booked_seats(Seat model)
        ids_booked_seats = [bs.seat.id for bs in booked_seats]

        hall = MovieSession.objects.get(id=pk_session).hall

        free_seats = Seat.objects.filter(hall__id=hall.id).exclude(id__in=ids_booked_seats)
        booked_seats = Seat.objects.filter(id__in=ids_booked_seats)
        return free_seats, booked_seats
