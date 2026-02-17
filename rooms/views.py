from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Room
from .serializers import RoomSerializer
from accounts.permissions import IsAdmin, IsManager
from rest_framework.permissions import BasePermission

class IsAdminOrManager(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and (request.user.is_staff or request.user.groups.filter(name='Manager').exists()))
    
class RoomViewSet(ModelViewSet):
    queryset = Room.objects.filter(is_active=True)
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        """
        Only Admin and Manager can create, update, delete rooms.
        All authenticated users can view rooms.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminOrManager]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [perm() for perm in permission_classes]
