from django.db import models

class Room(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('Maintenance', 'Maintenance'),
    ]
    room_number = models.CharField(max_length=20, null=True, blank=True)
    room_type = models.CharField(max_length=50, default='Standard')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, default=10000)
    image = models.ImageField(upload_to='rooms/', default='rooms/default.jpg')
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    """status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'
    )"""
    
    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"