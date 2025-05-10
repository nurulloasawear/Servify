from rest_framework import viewsets
from proffessions.models import Proffesions
from .serializers import *


class ProffessionViewSet(viewsets.ModelViewSet):
    queryset = Proffesions.objects.all()
    serializer_class = ProfessionSerializer

