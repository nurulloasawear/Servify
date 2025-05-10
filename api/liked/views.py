from rest_framework import viewsets
from liked.models import LikedAd
from .serializers import *
from api.permissions import * 
class LikedViewSet(viewsets.ModelViewSet):
    queryset = LikedAd.objects.all()
    serializer_class = LikedItemSerializer
    permission_classes =[IsClient,IsSpecialist]

