import base64
import json
from datetime import datetime, date
from turtle import pd
import holidays

from cinema.services.PriceService import PriceClassService

from ..models import Booking, Seat, MovieSession, SectorChoice, BookingHistory, ActionChoice
from django.contrib.auth import get_user_model

from ..serializers import BookingSerializer, SeatListSerializer

User = get_user_model()

COUNT_COLLUMNS_HALL = 3


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

    free_seats = Seat.objects.filter(
        hall__id=hall.id).exclude(id__in=ids_booked_seats)
    booked_seats = Seat.objects.filter(id__in=ids_booked_seats)
    return free_seats, booked_seats


class BookingClassService:

    @staticmethod
    def create_booking(session_id: int, request):
        # user_id = _get_user_id_from_token(request)
        user_id = 2
        booking_instance_ids = request.data
        print(booking_instance_ids)
        booked_inst = {}
        created_book = []
        for booked_id in booking_instance_ids:
            booked_inst['user'] = user_id
            booked_inst['session'] = session_id
            booked_inst['seat'] = booked_id
            ser = BookingSerializer(
                data=booked_inst,
                context={'user': User.objects.get(
                    id=user_id), 'session': session_id}
            )
            if ser.is_valid(raise_exception=True):
                instance = ser.save()
                booking_history = BookingHistory.objects.create(
                    action=ActionChoice.CREATE.value,
                    user=instance.user,
                    session=instance.session,
                    seat=instance.seat,
                    price=instance.price,
                    datetime_book=instance.datetime_book
                )
                booking_history.save()
                created_book.append(ser.data)

        return created_book

    @staticmethod
    def get_ids_booked_seats(pk_session: int):
        booked_seats = Booking.objects.filter(session=pk_session)
        booked_seats_list = [seat.seat.id for seat in booked_seats]
        return booked_seats_list

    @staticmethod
    def get_free_seats(pk_session: int):
        booked_seats = Booking.objects.filter(session=pk_session)
        ms_hall = MovieSession.objects.filter(id=pk_session).hall
        free_seats = Seat.objects.filter(hall=ms_hall)

    @staticmethod
    def get_free_booked_seats(pk_session: int) -> object:
        ''' not id -> to object'''
        # get id of booked_seats in the movie_session
        booked_seats = Booking.objects.filter(session=pk_session)

        # get id of booked_seats(Seat model)
        ids_booked_seats = [bs.seat.id for bs in booked_seats]

        hall = MovieSession.objects.get(id=pk_session).hall

        free_seats = Seat.objects.filter(
            hall__id=hall.id).exclude(id__in=ids_booked_seats)
        booked_seats = Seat.objects.filter(id__in=ids_booked_seats)
        return free_seats, ids_booked_seats
    
    

    @staticmethod
    def create_seat_layout(seats, pk_session):
        """
        Create structure to represent the layout (rows/columns) of seats.
        Make seat's price
        """
        seat_columns = COUNT_COLLUMNS_HALL
        ids_booked_seats = BookingClassService.get_ids_booked_seats(pk_session)
        print(ids_booked_seats)
        current_column = 0
        seat_layout, seat_row = [], []
        for seat in seats:
            ser= SeatListSerializer(seat)
            print(ser.data['id'])
            if ser.data['id'] in ids_booked_seats:
                ser.data['isBooked'] = True
                print('true')
            else:
                ser.data['isBooked'] = False
                print('false')
            print('service', ser.data)
            seat_row.append(ser.data)
            seat.price = PriceClassService.make_price_seat(seat)
            current_column += 1
            if current_column == seat_columns:
                seat_layout.append(seat_row)
                seat_row = []
                current_column = 0
        return seat_layout
