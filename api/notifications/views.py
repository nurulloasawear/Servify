from rest_framework import viewsets
from notifications.models import Notification
from .serializers import NotificationSerializer
from api.permissions import *
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes =[IsClient,IsSpecialist]
