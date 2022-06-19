from django.urls import path, include
from rest_framework import routers
from .views import RegisterView, UserProfile, user_is_admin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.SimpleRouter()
router.register(r'profile', UserProfile, basename='profile')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view({'post': 'create'})),
    path('is_admin/', user_is_admin, name='is_admin'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += router.urls
