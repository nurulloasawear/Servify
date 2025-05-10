from rest_framework import viewsets
from .serializers import *
from booking_m.models import *
from api.permissions import *


class BokingViewSets(viewsets.ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = Booking 
	permission_classes =[IsAdminOrReadOnly,IsOwnerOrReadOnly]


class BokingItemViewSets(viewsets.ModelViewSet):
	queryset = BookingItem.objects.all()
	serializer_class = Booking
	permission_classes =[IsAdminOrReadOnly,IsOwnerOrReadOnly]

