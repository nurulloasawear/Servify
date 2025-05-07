from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User as BaseUserManager
# Create your models here.
class Users(AbstractBaseUser):
    roles = [("is_Admin",0),('is_specialist',1),('is_client',2)]
    role = models.SmallIntegerField(choices=roles,default=2)
    full_name = models.CharField(max_length=50,null=False,blank=False)
    phone = models.CharField(null=False,max_length=30,unique=True)
    email = models.EmailField(unique=True)
    def __str__(self):
        return f"id:{self.id} - {self.full_name}"
class Profile(models.Model):
    user = models.OneToOneField(BaseUserManager,on_delete=models.CASCADE)
    
class user_interesting_analyz(models.Model):
    user = models.OneToOneField(BaseUserManager,on_delete=models.CASCADE)
 
class user_action_time_set_ad(models.Model):
    user = models.OneToOneField(BaseUserManager,on_delete=models.CASCADE)

