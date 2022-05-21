from datetime import datetime, timedelta

from cinema.models import MovieSession


def get_range_dates():
    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=5)

    # start = datetime.strptime(start_date, '%A, %d %B %Y')
    start = datetime.strptime(str(start_date), '%Y-%m-%d')
    end = datetime.strptime(str(end_date), '%Y-%m-%d')

    daterange = [(start + timedelta(days=x)).strftime('%Y-%m-%d') for x in range(0, (end - start).days)]
    print(daterange)
    return daterange


class CinemaService:

    @staticmethod
    def get_cinema_sessions(cinema_id:int):
        ms = MovieSession.objects.filter(
            hall__cinema__id=cinema_id, datetime_session__gte=datetime.now()
        )
        print(ms)
        return ms

    

