"""from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Booking
from .serializers import BookingSerializer
from accounts.permissions import IsAdmin, IsManager, IsStaff
from rest_framework import viewsets
from .services import is_room_available
from .models import Room

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.select_related('room', 'user')
    
    def get_permissions(self):
        
        Admin/Manager can create and manage bookings.
        Staff can only view bookings.
        
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin | IsManager]
        else:
            permission_classes = [IsAuthenticated]
        return [perm() for perm in permission_classes]

    def perform_create(self, serializer):
        room_id = serializer.validated_data['room'].id
        check_in = serializer.validated_data['check_in']
        check_out = serializer.validated_data['check_out']

        if not is_room_available(room_id, check_in, check_out):
            raise ValueError("Room is not available for the selected dates")
        serializer.save()

        nights = (check_out - check_in).days
        if nights <= 0:
            raise ValueError("Check-out date must be after check-in date")
        
        amount = nights * room.price_per_night # room.price must exist
        
        serializer.save(
            user=self.request.user,
            amount=amount
        )"""
        
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