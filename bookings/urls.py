"""from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet

router = DefaultRouter()
router.register(r'', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.booking_list, name='booking-list'),
]"""

# bookings/urls.py
from django.urls import path
from .views import create_public_booking

urlpatterns = [
    path('public/book/', create_public_booking),
]
