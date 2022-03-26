from rest_framework import routers
# from .views import
from .views import CinemaView, HallView
from movie.views import MovieView

router = routers.SimpleRouter()

router.register(r'movie', MovieView, basename='movie')
router.register(r'cinema', CinemaView, basename='cinema')
router.register(r'hall', HallView, basename='hall')

urlpatterns = router.urls
