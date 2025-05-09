from django.db import models
from users.models import Users

class AdminLog(models.Model):
    admin = models.ForeignKey(Users, on_delete=models.CASCADE)
    action = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)