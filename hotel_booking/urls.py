from django.urls import path
from rooms.views import RoomListCreateView

app_name = 'rooms'

urlpatterns = [
    path('api/rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    # Добавьте другие URL-маршруты по мере необходимости
]
