from rest_framework import viewsets
from location.models import Location
from .serializers import *


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

