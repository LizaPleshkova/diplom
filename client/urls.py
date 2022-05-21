from django.urls import path, include
from rest_framework import routers
from .views import RegisterView, UserProfile

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.SimpleRouter()
router.register(r'profile', UserProfile, basename='profile')

urlpatterns = [
    path('register/', RegisterView.as_view({'post': 'create'})),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += router.urls
