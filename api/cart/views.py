
from rest_framework import viewsets
from cart.models import *
from .serializers import *


# Define ViewSets
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

