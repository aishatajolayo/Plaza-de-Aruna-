# payments/urls.py
from django.urls import path
from .views import PaymentListView, InitializePaymentView, VerifyPaymentView

urlpatterns = [
    path('initialize/', InitializePaymentView.as_view(), name='initialize-payment'),
    path('verify/', VerifyPaymentView.as_view(), name='verify-payment'),
    path('', PaymentListView.as_view(), name='payment-list'),
]
