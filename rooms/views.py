from rest_framework import generics, filters
from .serializers import RoomSerializer, BookingSerializer
from .models import Room, Booking


class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [filters.OrderingFilter]
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


class BookingCancelView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
