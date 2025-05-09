from django.db import models
from services.models import Service

class Schedule(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

