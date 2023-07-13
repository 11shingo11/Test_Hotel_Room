from django.contrib import admin
from django.urls import include, path
from rooms.views import RoomListCreateView, RoomListAPIView, AvailableRoomListAPIView, BookingCreateView, \
    BookingCancelView

app_name = 'rooms'

urlpatterns = [
    path('api/rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('api/rooms/list/', RoomListAPIView.as_view(), name='room-list'),
    path('api/rooms/available/', AvailableRoomListAPIView.as_view(), name='available-room-list'),
    path('api/bookings/create/', BookingCreateView.as_view(), name='booking-create'),
    path('api/bookings/cancel/<int:pk>/', BookingCancelView.as_view(), name='booking-cancel'),
    # Добавьте другие URL-маршруты по мере необходимости
]