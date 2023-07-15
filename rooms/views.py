from .serializers import RoomSerializer, BookingSerializer, UserSerializer
from .models import Room, Booking
from rest_framework import generics, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import AvailabilityFilter


class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUser]


class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [filters.OrderingFilter, AvailabilityFilter]
    ordering_fields = ['price_per_night', 'capacity']


class AvailableRoomListAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price_per_night', 'capacity']

    def get_queryset(self):
        # Получаем начальную и конечную даты из параметров запроса
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        # Получаем список комнат, которые свободны в указанный интервал времени
        if start_date and end_date:
            bookings = Booking.objects.filter(
                start_date__lte=end_date,
                end_date__gte=start_date
            )
            booked_room_ids = bookings.values_list('room_id', flat=True)
            queryset = Room.objects.exclude(id__in=booked_room_ids)
        else:
            # Если не указаны даты, возвращаем все комнаты
            queryset = Room.objects.all()

        return queryset


class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class BookingListAPIView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Booking.objects.filter(user=user)


class BookingCancelView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)