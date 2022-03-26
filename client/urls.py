from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import RegisterView

router = routers.SimpleRouter()

urlpatterns = [
    path(r'register/', RegisterView.as_view({'post': 'create'})),
    path(r'token-auth/', obtain_jwt_token),
    path(r'token-refresh/', refresh_jwt_token),
]
# router.register(r'client', ..., basename='client')
#
# urlpatterns += router.urls
