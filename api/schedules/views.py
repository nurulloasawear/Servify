from rest_framework import viewsets
from schedules.models import Schedule
from .serializers import *


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

