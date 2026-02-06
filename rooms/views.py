from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Room
from .serializers import RoomSerializer
from accounts.permissions import IsAdmin, IsManager

class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        """
        Only Admin and Manager can create, update, delete rooms.
        All authenticated users can view rooms.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin | IsManager]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [perm() for perm in permission_classes]
