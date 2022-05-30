import datetime
from datetime import datetime

from django.contrib.auth import get_user_model

from cinema.models import Booking

from cinema.services.BookingService import BookingClassService
from django.core.mail import send_mail, BadHeaderError

import pdfkit
from CityCinema import settings

User = get_user_model()


class UserService:

    @staticmethod
    def download_tickets():
        filename = f'static/tickets/{datetime.now().date()}.pdf'
        config = pdfkit.configuration(
            wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        )
        print('FILename   ', filename)
        # return pdfkit.from_url('http://localhost:8080/profile/tickets/', f'static/tickets/{user}{datetime.now().date}.pdf', configuration=config)
        pdfkit.from_url(
            'http://127.0.0.1:8000/client/profile/booked-tickets/',
            # 'http://google.com',
            filename, configuration=config
        )
        return filename

        # wkhtmltopdf = WKHtmlToPdf(
        #     url='http://google.com',
        #     output_file='out.pdf',
        # )
        # wkhtmltopdf.render()

    @staticmethod
    def send_tickets_to_email(user):
        '''
ЛОГИЧНЕЕ БУДЕТ НЕ СОХРАНЯТЬ ФАЙЛ НА ПК, А СОЗДАВАТЬ ЭКЗЕМПЛЯР ФАЙЛА И ЕГО ОТПРАВЛЯТЬ

        тут будет отправка одного конкретного билета
        сначала будет генерироваться файл с билетами -> потом отпрака на почту
        '''
        subject = "Пробное сообщение"
        body = {
            'user': user.username,
            'email': user.email,
            'message': 'try to send message',
        }
        message = "\n".join(body.values())
        try:
            send_mail(
                subject, message, from_email=settings.EMAIL_HOST_USER, recipient_list=['pl.1.el.vas@gmail.com']
            )
            # 'admin@example.com',
            # ['admin@example.com'])
        except BadHeaderError:
            raise BadHeaderError

    @staticmethod
    def get_booked_tickets(booked_ids):
        '''
        return booking data to create booked_tickets
        '''

        bookings = Booking.objects.filter(id__in=booked_ids)
        return bookings

    @staticmethod
    def get_user_current_booked_seats(user):
        current_booked = BookingClassService.get_current_booking().filter(user=user)
        # current_booked = Booking.objects.filter(
        #      session__datetime_session__gte=datetime.datetime.now()
        # )
        for i in current_booked:
            date = i.datetime_book
            i.datetime_book = date.strftime("%m-%d-%y, %H:%M")
        return current_booked

    @staticmethod
    def get_user_history_booked_seats(user):
        # booking_rec = Booking.objects.select_related('session', 'seat').filter(
        #     user=user, session__datetime_session__lt=datetime.datetime.now()
        # )
        booking_rec = Booking.objects.select_related('session', 'seat').filter(
            user=user
        )
        for i in booking_rec:
            date = i.datetime_book
            i.datetime_book = date.strftime("%m-%d-%y, %H:%M")
        return booking_rec
