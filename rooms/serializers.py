from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    room_type_display = serializers.CharField(source='get_room_type_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Room
        fields = [
            'id',
            'room_number',
            'room_type', 
            'description',
            'price',
            'status', 
            'image'
        ]
