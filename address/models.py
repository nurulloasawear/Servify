from django.db import models
from users.models import Users

class Address(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)