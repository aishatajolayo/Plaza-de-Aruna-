# bookings/serializers.py
from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'room',
            'guest_name',
            'guest_email',
            'check_in',
            'check_out',
            'nights',
            'total_price',
        ]
        read_only_fields = ['nights','total_price']

    def validate(self, data):
        room = data['room']
        
        if room.status != 'available':
            raise serializers.ValidationError(
                "This room is not available for booking."
            )
            
        if data['check_out'] <= data['check_in']:
            raise serializers.ValidationError(
                "Check-out date must be after check-in date"
            )
        return data

