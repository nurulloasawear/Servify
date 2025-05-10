from rest_framework import viewsets
from liked.models import LikedAd
from .serializers import *

class LikedViewSet(viewsets.ModelViewSet):
    queryset = LikedAd.objects.all()
    serializer_class = LikedItemSerializer

