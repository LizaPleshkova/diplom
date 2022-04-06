from django.contrib import admin
from .models import (
    Hall, MovieSession, Seat, ScheduleRental, Sector, SessionSchedule, Cinema, Booking, BookingHistory
)


class CinemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']


class HallAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cinema', 'count_places')
    list_filter = ['id', 'cinema']
    search_fields = ['name']


class SectorAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description',
    )
    search_fields = ['name']


class SeatAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'hall', 'sector', 'number_place', 'number_row',
    )
    list_filter = ['hall', 'sector']
    search_fields = ['hall', 'sector']


class MovieSessionCompositionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'hall', 'movie', 'datetime_session',
    )
    list_filter = ['hall', 'movie', 'datetime_session',]
    search_fields = ['hall', 'movie', 'datetime_session',]


class ScheduleRentalAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'movie', 'start_date', 'end_date',
    )
    list_filter = ['id', 'movie']
    search_fields = ['movie']


class SessionScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'start_time', 'end_time',
    )
    search_fields = ['name']


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'session', 'seat', 'price', 'datetime_book',
    )
    search_fields = ['user', 'session']
    list_filter = ['user', 'session']


class BookingHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'session', 'seat', 'action'
    )
    search_fields = ['user', 'session', 'action']
    list_filter = ['user', 'session', 'action']


admin.site.register(BookingHistory, BookingHistoryAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Cinema, CinemaAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(MovieSession, MovieSessionCompositionAdmin)
admin.site.register(ScheduleRental, ScheduleRentalAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(SessionSchedule, SessionScheduleAdmin)
