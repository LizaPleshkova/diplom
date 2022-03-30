from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('cinema.urls')),
                  # path('cinemas/', include('cinema.urls')),
                  path('client/', include('client.urls')),
                  # path('movies/', include('movie.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
