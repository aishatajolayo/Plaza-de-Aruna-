import requests
from django.conf import settings

PAYSTACK_SECRET = "YOUR_SECRET_KEY"

BASE_URL = "https://api.paystack.co"

def initialize_payment(email, amount, reference):
    url = f"{BASE_URL}/transaction/initialize"

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "email": email,
        "amount": int(amount * 100),  # Paystack uses kobo
        "reference": reference,
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()


def verify_payment(reference):
    url = f"{BASE_URL}/transaction/verify/{reference}"

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
    }

    response = requests.get(url, headers=headers)
    return response.json()
