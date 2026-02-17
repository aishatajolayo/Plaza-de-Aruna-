# bookings/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import BookingSerializer

@api_view(['POST'])
@permission_classes([AllowAny])  # 🔓 PUBLIC
def create_public_booking(request):
    serializer = BookingSerializer(data=request.data)

    if serializer.is_valid():
        booking = serializer.save()
        return Response({
            "message": "Booking created successfully",
            "booking_id": booking.id,
            "nights": booking.nights,
            "total_price": booking.total_price
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)