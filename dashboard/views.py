from django.shortcuts import render
from django.utils.timezone import now
from django.db.models import Sum, Count
from bookings.models import Booking
from rooms.models import Room
from payments.models import Payment
from decimal import Decimal
import json
from django.db.models import Sum
from django.db.models.functions import ExtractMonth
from django.utils import timezone
from datetime import timedelta
from django.utils.timezone import now

def dashboard_view(request):
    today = now().date()
    
    active_bookings = Booking.objects.filter(
        check_in__lte=today,
        check_out__gt=today,
        status__in=['confirmed', 'checked_in']
    )

    active_guests = active_bookings.count()
    occupied_rooms = active_bookings.count()
    #total_bookings = Booking.objects.count()

    total_rooms = Room.objects.count()
    occupied_rooms = Room.objects.filter(status='occupied').count()
    occupancy_rate = (
        (occupied_rooms / total_rooms) * 100 if total_rooms > 0 else 0
    )

    total_revenue = Payment.objects.filter(
        status='successful'
    ).aggregate(total=Sum('amount'))['total'] or 0

    active_guests = Booking.objects.filter(
        status__in=['confirmed', 'checked-in']
    ).values('user').distinct().count()

    # Room status
    room_status = {
        'occupied': Room.objects.filter(status='occupied').count(),
        'available': Room.objects.filter(status='available').count(),
        'maintenance': Room.objects.filter(status='maintenance').count(),
    }

    # Monthly revenue (Jan–Dec)
    revenue_qs = (
        Booking.objects
        .annotate(month=ExtractMonth('created_at'))
        .values('month')
        .annotate(total=Sum('payment__amount'))
        .order_by('month')
    )

    monthly_revenue = [0] * 12

    for item in revenue_qs:
        monthly_revenue[item['month'] - 1] = float(item['total'])

    recent_bookings = Booking.objects.select_related(
        'room', #'payment'
    ).order_by('-created_at')[:5]
    
    today = timezone.now().date()
    current_month_start = today.replace(day=1)
    last_month_end = current_month_start - timedelta(days=1)
    last_month_start = last_month_end.replace(day=1)
    
    current_month_bookings = Booking.objects.filter(
        created_at__gte=current_month_start
        ).count()

    last_month_bookings = Booking.objects.filter(
        created_at__range=(last_month_start, last_month_end)
    ).count()

    bookings_percent_change = (
        ((current_month_bookings - last_month_bookings) / last_month_bookings) * 100
        if last_month_bookings > 0 else 0
    )

    total_rooms = Room.objects.count()
    
    occupied_now = Booking.objects.filter(
        status="checked_in"
    ).count()

    current_occupancy_rate = (
        (occupied_now / total_rooms) * 100
        if total_rooms > 0 else 0
    )

    last_week_start = today - timedelta(days=7)

    occupied_last_week = Booking.objects.filter(
        status="checked_in",
        created_at__gte=last_week_start
    ).count()

    last_week_occupancy_rate = (
        (occupied_last_week / total_rooms) * 100
        if total_rooms > 0 else 0
    )

    occupancy_percent_change = current_occupancy_rate - last_week_occupancy_rate
    
    current_month_revenue = Payment.objects.filter(
        status="successful",
        created_at__gte=current_month_start
    ).aggregate(total=Sum("amount"))["total"] or 0

    last_month_revenue = Payment.objects.filter(
        status="successful",
        created_at__range=(last_month_start, last_month_end)
    ).aggregate(total=Sum("amount"))["total"] or 0

    revenue_percent_change = (
        ((current_month_revenue - last_month_revenue) / last_month_revenue) * 100
        if last_month_revenue > 0 else 0
    )
    
    """active_guests = Booking.objects.filter(
        status="checked_in"
    ).count()

    occupied_rooms = active_guests"""  # 1 guest = 1 room

    context = {
        'date_today': now(),
        'total_bookings': current_month_bookings,
        'occupancy_rate': round(occupancy_rate, 1),
        'total_revenue': current_month_revenue,
        'active_guests': active_guests,
        'room_status': room_status,
        'monthly_revenue': monthly_revenue,
        'revenue_data': json.dumps(monthly_revenue),
        'recent_bookings': recent_bookings,
        
        'bookings_percent_change': round(bookings_percent_change, 1),
        "occupancy_percent_change": round(occupancy_percent_change, 1),
        "revenue_percent_change": round(revenue_percent_change, 1),
        
        "occupied_rooms": occupied_rooms,
    }

    return render(request, 'dashboard/index.html', context)

def room_management_view(request):
    rooms = Room.objects.all()

    context = {
        'rooms': rooms,
        'total_rooms': rooms.count(),
        'available_rooms': rooms.filter(status='available').count(),
        'occupied_rooms': rooms.filter(status='occupied').count(),
        'maintenance_rooms': rooms.filter(status='maintenance').count(),
    }
    
    return render(request, 'dashboard/room_management.html', {
        'date_today': now()
    })