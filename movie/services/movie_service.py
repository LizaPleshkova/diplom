import datetime

from movie.models import Movie
# from CinemaProject import cinema
from cinema.models import MovieSession

from cinema.models import ScheduleRental


class MovieService:
    @staticmethod
    def get_latest_movies():
        ''' for '''
        latest_movies = ScheduleRental.objects.order_by(
            'start_date', 'end_date'
        ).distinct().values('id_movie')[:3]
        movies = Movie.objects.filter(id_movie__in=latest_movies)
        # latest_movies = MovieSession.objects.order_by('datetime_session').select_related('id_movie')[:3]
        # print(latest_movies)
        # print(movies)

        return movies

    @staticmethod
    def get_movies_now():
        ''' movies that are in the rental now
        ? которые вооюще в прокате или есть сейансы егодня
        '''
        today = datetime.datetime.now().date()
        mv = MovieSession.objects.filter(
            datetime_session__date=today
        ).distinct().values('id_movie')
        movies = Movie.objects.filter(id_movie__in=mv)
        # print(mv)
        # print(today)
        return movies

    @staticmethod
    def get_sessions_movie(pk: int):
        mv = MovieSession.objects.filter(
            id_movie=pk, datetime_session__gte=datetime.datetime.now(),

        )
        return mv
