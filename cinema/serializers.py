from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Cinema, Hall, Sector, Seat, SessionSchedule, MovieSession, ScheduleRental

User = get_user_model()


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


class SeatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class SessionScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionSchedule
        fields = '__all__'


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = '__all__'


class ScheduleRentalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleRental
        fields = '__all__'

