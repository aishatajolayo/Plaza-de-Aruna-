# bookings/urls.py
from django.urls import path
from .views import create_public_booking

urlpatterns = [
    path('public/book/', create_public_booking),
]
