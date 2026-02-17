from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Subscriber
from .serializers import SubscriberSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def subscribe(request):
    email = request.data.get("email")

    if Subscriber.objects.filter(email=email).exists():
        return Response(
            {"message": "You are already subscribed"},
            status=status.HTTP_200_OK
        )

    Subscriber.objects.create(email=email)
    return Response(
        {"message": "Successfully subscribed"},
        status=status.HTTP_201_CREATED
    )
