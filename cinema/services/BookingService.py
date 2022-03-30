from datetime import datetime, date
from turtle import pd
import holidays
from ..models import Booking, Seat, MovieSession
from ..models import SectorChoice


def _weekends(start, end):
    df = pd.DataFrame({'Dates': pd.date_range(start, end)})
    busines_dates = pd.bdate_range(start, end)
    answer = df.loc[~df['Dates'].isin(busines_dates)]
    print("There are", answer.shape[0], 'weekends between', start, 'and', end)
    return answer


def _get_holidays_weekends():
    ''' get holidays and weekends for price '''
    holidays_list = holidays.Russia(years=datetime.datetime.now().year).items()
    print(holidays_list)
    weekends_list = _weekends(
        date(year=datetime.datetime.now().year, month=1, day=1),
        date(year=datetime.datetime.now().year, month=12, day=31)
    )
    print(weekends_list)

    all_dates = list(set(holidays_list + weekends_list))
    return all_dates


class PriceService:
    @staticmethod
    def make_price_seat(seat):

        if seat.sector.name == SectorChoice.VIP.value:
            price = float(12.00)
        # seat in the center, expensive
        elif seat.sector.name == SectorChoice.A.value:
            price = float(7.00)
        # seat near the center, standart
        elif seat.sector.name == SectorChoice.B.value:
            price = float(6.00)
        # last seats, the cheapest
        elif seat.sector.name == SectorChoice.C.value:
            price = float(5.50)
        else:
            raise ValueError('seector is not defined')
        return price


class BookingService:

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
    def get_free_booked_seats(pk_session: int):
        # get id of booked_seats in the movie_session
        booked_seats = Booking.objects.filter(session=pk_session)

        # get id of booked_seats(Seat model)
        ids_booked_seats = [bs.seat.id for bs in booked_seats]

        hall = MovieSession.objects.get(id=pk_session).hall

        free_seats = Seat.objects.filter(hall__id=hall.id).exclude(id__in=ids_booked_seats)
        booked_seats = Seat.objects.filter(id__in=ids_booked_seats)
        return free_seats, booked_seats

