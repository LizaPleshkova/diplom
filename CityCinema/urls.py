from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cinemas/', include('cinema.urls')),
    # path('client/', include('client.urls')),
    path('movies/', include('movie.urls')),

]
