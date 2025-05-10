from rest_framework import viewsets
from notifications.models import Notification
from .serializers import *

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

