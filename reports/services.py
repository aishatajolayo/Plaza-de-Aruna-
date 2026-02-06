from payments.models import Payment
from django.db.models import Sum

def monthly_revenue(month):
    return Payment.objects.filter(
        status='successful',
        created_at__month=month
    ).aggregate(Sum('amount'))
