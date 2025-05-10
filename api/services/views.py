from rest_framework import viewsets
from .serializers import *
from services.models import Service
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
