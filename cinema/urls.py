from django.urls import path, include
from rest_framework import routers
# from .views import
from .views import CinemaView, HallView, MovieSessionView, BookingView, filters_data
from movie.views import MovieView

router = routers.SimpleRouter()
router.register(r'movie', MovieView, basename='movie')
router.register(r'cinema', CinemaView, basename='cinema')
router.register(r'movie-session', MovieSessionView, basename='movie-session')

router.register(r'hall', HallView, basename='hall')
router.register(r'booking', BookingView, basename='booking')

urlpatterns = [
   path('filters/', filters_data, name='filters'),
]

urlpatterns += router.urls