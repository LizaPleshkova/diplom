import base64
import json
from datetime import datetime, date
import datetime
from msilib.schema import InstallUISequence
from turtle import pd
import holidays

from cinema.services.PriceService import PriceClassService

from ..models import Booking, Seat, MovieSession, SectorChoice, BookingHistory, ActionChoice
from django.contrib.auth import get_user_model

from ..serializers import BookingSerializer, SeatListSerializer

User = get_user_model()

COUNT_COLLUMNS_HALL = 3
MINUTS_CANCELED_BOOKING = 30


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
    #
    # def __init__(self):
    #     print('hereeee  ')
    #     BookingClassService.update_all_booking()
    #
    # def __call__(self):
    #     print('hereeee  ')
    #     BookingClassService.update_all_booking()

    @staticmethod
    def get_current_booking():
        current_booked_seats = Booking.objects.select_related('session', 'seat').filter(
            session__datetime_session__gte=datetime.datetime.now()
        )
        return current_booked_seats

    @staticmethod
    def update_all_booking():
        '''
        отменить бронироввание если isPaid = False за 30 минут до начала киносеанса
        '''
        current_booking = BookingClassService.get_current_booking().filter(isPaid=False)
        date_now = datetime.datetime.now()

        for booking in current_booking:
            print('date now', date_now, booking.session.datetime_session,
                  booking.session.datetime_session.replace(tzinfo=None))
            print(booking)
            if abs(
                    booking.session.datetime_session.replace(tzinfo=None) - date_now
            ).min <= datetime.timedelta(minutes=MINUTS_CANCELED_BOOKING):
                BookingClassService.delete_booking(booking)
                print(booking.session.datetime_session.replace(tzinfo=None) - date_now)
        print('end updating booking')

    @staticmethod
    def delete_booking(instance: Booking):

        print(instance)
        booking_history = BookingHistory.objects.create(
            action=ActionChoice.DELETE.value,
            user=instance.user,
            session=instance.session,
            seat=instance.seat,
            price=instance.price,
            datetime_book=instance.datetime_book
        )
        print(booking_history)
        booking_history.save()
        instance.delete()
        print('------------- END DELETE BOOKING ------------ ')

    @staticmethod
    def get_seats(session_id: int):
        ms_hall = MovieSession.objects.filter(id=session_id)

    @staticmethod
    def create_booking(session_id: int, request):
        user_id = request.user.id
        booking_instance_ids = request.data
        # booking_instance_ids = [9,10]
        print(booking_instance_ids)
        # print(booking_instance_ids)
        booked_inst = {}
        created_book = []
        for booked_id in booking_instance_ids:
            booked_inst['user'] = user_id
            booked_inst['session'] = session_id
            booked_inst['seat'] = booked_id
            # print(booked_id)
            # for postman
            # booked_inst['seat'] = booking_instance_ids['seat']
            print(booked_inst)
            ser = BookingSerializer(
                data=booked_inst,
                context={'user': User.objects.get(
                    id=user_id), 'session': session_id}
            )
            print('after')
            if ser.is_valid(raise_exception=True):
                seat = Seat.objects.get(id=ser.validated_data['seat'].id)
                seat.isBooked = True
                seat.save(update_fields=['isBooked'])
                instance = ser.save()
                print('after save inst')

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
        print(booked_seats)

        # get id of booked_seats(Seat model)
        ids_booked_seats = [bs.seat.id for bs in booked_seats]

        hall = MovieSession.objects.get(id=pk_session).hall

        free_seats = Seat.objects.filter(
            hall__id=hall.id).exclude(id__in=ids_booked_seats)
        booked_seats = Seat.objects.filter(id__in=ids_booked_seats)
        return free_seats, ids_booked_seats

    @staticmethod
    def create_seat_layout(seats, pk_session: int):
        """
        Create structure to represent the layout (rows/columns) of seats.
        Make seat's price
        """
        seat_columns = COUNT_COLLUMNS_HALL
        # ids_booked_seats = BookingClassService.get_ids_booked_seats(pk_session)
        # print(ids_booked_seats)
        current_column = 0
        seat_layout, seat_row = [], []
        for seat in seats:
            ser = SeatListSerializer(seat)
            seat_valid = ser.data
            seat_valid['price'] = PriceClassService.make_price_seat(seat)
            seat_row.append(seat_valid)
            current_column += 1
            if current_column == seat_columns:
                seat_layout.append(seat_row)
                seat_row = []
                current_column = 0
        return seat_layout
