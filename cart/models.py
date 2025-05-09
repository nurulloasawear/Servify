from django.db import models
from users.models import Users
from services.models import Service

class Cart(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
