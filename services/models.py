from django.db import models
from category.models import Category
from proffessions.models import Proffesions as Profession
# from proffessions
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True)
    def __str__(self):
    	return self.title

