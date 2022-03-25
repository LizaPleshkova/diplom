from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import MovieView

router = routers.SimpleRouter()


router.register(r'movie', MovieView, basename='movie')
#
# urlpatterns = [
#     path('movie/', MovieView.as_view(), name='movie')
# ]

urlpatterns = router.urls