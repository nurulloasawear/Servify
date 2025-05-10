from  rest_framework import viewsets
from address.models import Address
from .serializers import *
from api.permissions import *

class AddressViewSet(viewsets.ModelViewSet):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
	permission_classes  = [IsOwnerOrReadOnly,IsAdminOrReadOnly]