from django.contrib import admin
from .models import (
    Hall, MovieSession, Seat, ScheduleRental, Sector, SessionSchedule, Cinema, Booking, BookingHistory
)
from django.urls import reverse
from django.utils.html import format_html


class CinemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']


#
# class CinemaInline(admin.TabularInline):
#     model = Cinema  # related model
#     extra = 1  # number of new record fields
#

class HallAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link_to_cinema', 'count_places')
    list_filter = ['cinema']
    search_fields = ['name', 'cinema']

    # inlines = [CinemaInline, ]

    def link_to_cinema(self, obj):
        link_to_cinema = reverse("admin:cinema_cinema_change", args=[obj.cinema.id])
        return format_html('<a href="{}">{},{}</a>', link_to_cinema, obj.cinema.name, obj.cinema.address)
    link_to_cinema.short_description = 'кинотеатр'


class SectorAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description',
    )
    search_fields = ['name']


class SeatAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'hall', 'sector', 'number_place', 'number_row', 'isBooked'
    )
    list_filter = ['hall', 'sector', 'isBooked']
    search_fields = ['hall', 'sector']


class MovieSessionCompositionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'hall', 'movie', 'datetime_session',
    )
    list_filter = ['hall', 'movie', 'datetime_session', ]
    search_fields = ['hall', 'movie', 'datetime_session', ]


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
        'id', 'id_ticket', 'user', 'session', 'seat', 'price', 'datetime_book', 'isPaid'
    )
    search_fields = ['user', 'session']
    list_filter = ['user', 'session', 'isPaid']


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
