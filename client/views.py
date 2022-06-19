from wsgiref.util import FileWrapper
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework.decorators import action, api_view
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import viewsets, status

from .serializers import RegisterSerializer, UserListSerializer
from .services.UserService import UserService
from cinema.serializers import BookingReportSerializer

from cinema.services.BookingService import _get_user_id_from_token

User = get_user_model()


class UserProfile(ListModelMixin, RetrieveModelMixin, CreateModelMixin, viewsets.GenericViewSet, viewsets.ViewSet):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)

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
    def send_tickets_email(self, request):
        # недописанно   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

        # user = _get_user_id_from_token(request)
        user = request.user
        print("user = ", user)
        UserService.send_tickets_to_email(user)
        return Response(content_type='application/json', status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='booked-tickets')
    def get_booked_tickets(self, request):
        user = request.user
        booked_ids = request.data['booked_ids']
        # booked_ids = ['233']
        bookings = UserService.get_booked_tickets(booked_ids)
        bookings_serializer = BookingReportSerializer(bookings, many=True)
        return Response(bookings_serializer.data, content_type='application/json', status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='download-booked-tickets')
    def download_booked_tickets(self, request):
        # недописанно   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        print(request, dir(request))
        user = request.user
        print("user = ", user)
        filename = UserService.download_tickets()

        short_report = open(filename, 'rb')
        response = HttpResponse(FileWrapper(short_report), content_type='application/pdf', status=status.HTTP_200_OK)
        return response

    @action(methods=['get'], detail=False, url_path='report')
    def user_report(self, request):
        user = _get_user_id_from_token(request)
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

    # serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        user = request.data
        serializer = RegisterSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['GET'])
def user_is_admin(request):
    user = request.user
    return Response(
        user.is_superuser,
        content_type='application/json', status=status.HTTP_200_OK
    )
