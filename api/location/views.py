from rest_framework import viewsets
from location.models import Location
from .serializers import LocationSerializer
from .serializers import LocationSerializer
from api.permissions import IsClient,IsSpecialist

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes =[IsClient,IsSpecialist]
