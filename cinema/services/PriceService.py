from datetime import datetime, date
from turtle import pd
import holidays
from django.contrib.auth import get_user_model

from cinema.models import SectorChoice

User = get_user_model()


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
        '''
            через
        '''
        try:

            price = {
                SectorChoice.VIP.value: float(12.00),
                SectorChoice.A.value: float(7.00),
                SectorChoice.B.value: float(6.00),
                SectorChoice.C.value: float(5.50)
            }
            return price[seat.sector.name]
        except Exception as e:
            raise ValueError('seector is not defined')