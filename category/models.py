from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    is_main = models.BooleanField(default=False)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name="subcategorries")
    slug = models.SlugField(unique=True)
    def __str__(self):
        return f"{self.name} main:{self.is_main}"
