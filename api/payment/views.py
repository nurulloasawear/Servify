from rest_framework import viewsets
from payment.models import Payment
from .serializers import *

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

