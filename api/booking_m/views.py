from rest_framework import viewsets
from .serializers import *
from booking_m.models import *

class BokingViewSets(viewsets.ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = Booking 

class BokingItemViewSets(viewsets.ModelViewSet):
	queryset = BookingItem.objects.all()
	serializer_class = Booking

