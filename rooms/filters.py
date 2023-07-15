from rest_framework import filters
from .models import Booking


class AvailabilityFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if start_date and end_date:
            bookings = Booking.objects.filter(
                start_date__lte=end_date,
                end_date__gte=start_date
            )
            booked_room_ids = bookings.values_list('room_id', flat=True)
            queryset = queryset.exclude(id__in=booked_room_ids)

        return queryset
