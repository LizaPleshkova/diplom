from datetime import datetime

from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import viewsets, status, serializers
from dateutil.parser import parse

from .serializers import RegisterSerializer, UserListSerializer
from .services.UserService import UserService
from cinema.serializers import BookingReportSerializer

from cinema.services.BookingService import _get_user_id_from_token

User = get_user_model()


class UserProfile(ListModelMixin, RetrieveModelMixin, CreateModelMixin, viewsets.GenericViewSet, viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        queryset = User.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserListSerializer
        return UserListSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     movie_sessions = MovieService.get_sessions_movie(instance.id)
    #     data = {
    #         'movie': serializer.data,
    #         'movie_sessions': movie_sessions
    #     }
    #     return Response(data, content_type='application/json', status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='send_tickets')
    def send_tickets(self, request):
        # user = _get_user_id_from_token(request)
        user = request.user
        print("user = ", user)
        UserService.send_tickets_to_email(user)
        return Response(content_type='application/json', status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='report')
    def user_report(self, request):
        user = _get_user_id_from_token(request)
        print("user = ", user)
        booking_rec = UserService.get_user_history_booked_seats(user)
        current_booked_seats = UserService.get_user_current_booked_seats(user)

        serializer_history_booking = BookingReportSerializer(booking_rec, many=True)
        serializer_current_booking = BookingReportSerializer(current_booked_seats, many=True)
        report = {
            'booked_seat': serializer_history_booking.data,
            'current_booked': serializer_current_booking.data
        }
        return Response(report, content_type='application/json', status=status.HTTP_200_OK)


class RegisterView(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        print('req ', request.data)
        user = request.data
        print(user['birth_date'], type(user['birth_date']))
        dates = parse(user['birth_date'])
        # user['birth_date'] = dates.date()
        serializer = RegisterSerializer(data=user)
        # print(serializer.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
