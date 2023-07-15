from django.contrib import admin
from rooms.views import RoomListCreateView, RoomListAPIView, AvailableRoomListAPIView, BookingCreateView, \
    BookingCancelView, UserRegistrationView, UserLoginView, BookingListAPIView
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = 'rooms'

urlpatterns = [
    path('api/rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('api/rooms/list/', RoomListAPIView.as_view(), name='room-list'),
    path('api/rooms/available/', AvailableRoomListAPIView.as_view(), name='available-room-list'),
    path('api/bookings/create/', BookingCreateView.as_view(), name='booking-create'),
    path('api/bookings/cancel/<int:pk>/', BookingCancelView.as_view(), name='booking-cancel'),
    path('api/auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/auth/login/', UserLoginView.as_view(), name='user-login'),
    path('api/bookings/', BookingListAPIView.as_view(), name='booking-list'),
    path('admin/', admin.site.urls),
]
