from datetime import datetime
from movie.models import Movie, Comment
from cinema.models import MovieSession, ScheduleRental
from cinema.serializers import MovieSessionSerializer


class MovieService:

    @staticmethod
    def get_latest_movies():
        latest_movies = ScheduleRental.objects.order_by(
            '-start_date', '-end_date'
        ).distinct().values('movie')[:3]
        movies = Movie.objects.filter(id__in=latest_movies)
        return movies

    @staticmethod
    def get_movies_soon():
        latest_movies = ScheduleRental.objects.filter(start_date__gt=datetime.now()).order_by(
            '-start_date', '-end_date'
        ).distinct().values('movie')[:5]
        movies = Movie.objects.filter(id__in=latest_movies)
        return movies

    @staticmethod
    def get_movies_now():
        ''' movies that are in the rental now '''
        today = datetime.datetime.now().date()
        mv = MovieSession.objects.filter(
            datetime_session__date=today
        ).distinct().values('id')
        movies = Movie.objects.filter(id__in=mv)
        return movies

    @staticmethod
    def get_sessions_movie(movie_id: int):
        mv = MovieSession.objects.filter(
            movie=movie_id, datetime_session__gte=datetime.now(),
        )
        serializer = MovieSessionSerializer(mv, many=True)
        return serializer.data

    @staticmethod
    def get_comments_movie(movie_id: int):
        comments = Comment.objects.filter(
            movie=movie_id, is_visible=True
        ).order_by('-date')
        for i in comments:
            date = i.date
            i.date = date.strftime("%m-%d-%y, %H:%M")
        return comments
