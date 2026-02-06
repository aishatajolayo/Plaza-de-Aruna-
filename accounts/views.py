from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rooms.models import Room
from rooms.serializers import RoomSerializer
from accounts.permissions import IsAdmin, IsManager

class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]  # All logged-in users

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin | IsManager]  # Only Admin & Manager can edit
        else:
            permission_classes = [IsAuthenticated]  # All can view
        return [perm() for perm in permission_classes]
