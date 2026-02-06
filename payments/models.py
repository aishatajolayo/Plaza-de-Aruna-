from django.db import models
from bookings.models import Booking
from django.utils import timezone

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='payment')
    reference = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('successful', 'Successful'),
        ('failed', 'Failed'),
    )

    def __str__(self):
        return f"{self.booking} - {self.amount}"
