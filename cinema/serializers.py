from datetime import datetime

from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Cinema, Hall, Sector, Seat, SessionSchedule, MovieSession, ScheduleRental, Booking
from .services.PriceService import PriceService

User = get_user_model()


class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    datetime_book = serializers.DateTimeField(required=False)

    class Meta:
        model = Booking
        fields = ('user', 'session', 'seat', 'price', 'datetime_book')

    def validate(self, booking_instance):

        if booking_instance.get('session').id != int(self.context['session']):
            raise serializers.ValidationError('something wrong with movie session id', code='invalid')

        if booking_instance['user'] != self.context['user']:
            raise serializers.ValidationError('something wrong with user id', code='invalid')

        booked_seats = Booking.objects.filter(session=self.context['session'])
        booked_seats_list = [seat.seat.number_place for seat in booked_seats]

        if booking_instance['seat'].id in booked_seats_list:
            raise serializers.ValidationError('seat is already booked', code='invalid')

        price = PriceService.make_price_seat(booking_instance['seat'])
        booking_instance['price'] = price
        booking_instance['datetime_book'] = datetime.now()
        return booking_instance


class CinemaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class SectorlListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


class HallListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'


class HallCreateSerializer(serializers.Serializer):
    count_places = serializers.IntegerField(required=False, allow_null=False)
    name = serializers.CharField()
    cinema = serializers.CharField()

    def validate_cinema(self, value):
        print(value)

        if not Cinema.objects.filter(id=int(value)).exists():
            raise serializers.ValidationError("cinema doesn't exist", code='invalid')
        else:
            value = Cinema.objects.get(id=int(value))
        return value

    def validate_count_places(self, value):
        ''' not work '''
        print("validate_count_places", value)
        if value is not None:
            if value > 10:
                raise serializers.ValidationError('no more than 10 seats in the hall', code='invalid')
        else:
            value = 10
        return value

    def create(self, validated_data):
        return Hall.objects.create(**validated_data)

    # def validate(self, data):
    #     """ validate for all fields (cienema id"""
    #     """ checking count places """
    #     if data.get('count_places') is None:
    #         data['count_places'] = 10
    #     if data.get('count_places') > 10:
    #         raise serializers.ValidationError('no more than 10 seats in the hall', code='invalid')
    #     return data


class MovieSessionSerializer(serializers.ModelSerializer):
    hall = HallListSerializer()

    class Meta:
        model = MovieSession
        fields = ('id', 'hall', 'movie', 'datetime_session',)


class SeatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class SessionScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionSchedule
        fields = '__all__'


class ScheduleRentalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleRental
        fields = '__all__'
