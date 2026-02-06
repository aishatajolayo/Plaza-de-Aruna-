# bookings/services.py

from .models import Booking, Room
from datetime import datetime

def is_room_available(room_id, check_in, check_out):
    """
    Check if a room is available between check_in and check_out dates.
    """
    overlapping_bookings = Booking.objects.filter(
        room_id=room_id,
        check_in__lt=check_out,
        check_out__gt=check_in
    )
    return not overlapping_bookings.exists()
