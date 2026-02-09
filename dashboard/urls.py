from django.urls import path
from .views import dashboard_view
from .views import dashboard_view, room_management_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('rooms/', room_management_view, name='room-management'),
]
