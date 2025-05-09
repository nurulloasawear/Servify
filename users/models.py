from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
# from django.contrib.auth.models import User as BaseUserManager
# Create your models here.
class CustomeUserManager(BaseUserManager):
    def create_user(self,face_scan,password=None,**extra_fields):
        if not face_scan:
            raise ValueError("Undetected face in image")
        user = self.model(face_scan=face_scan,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 
    def create_superuser(self,face_scan,password,**extra_fields):
        extra_fields.set_default('is_staff',True)
        extra_fields.set_default('is_superuser',True)
        return self.create_user(face_scan,password,**extra_fields)
class Users(AbstractBaseUser,PermissionsMixin):
    face_scan = models.ImageField(upload_to='face_scan/',unique=True)
    face_encoding = models.BinaryField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  
    password = None
    USERNAME_FIELD = 'face_scan'
    REQUIRED_FIELDS = [] 

    objects = CustomeUserManager()
    def __str__(self):
        return f"User ID:{self.id}"






class UserProfile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True,default="")
    roles = [("is_Admin",0),('is_specialist',1),('is_client',2)]
    role = models.SmallIntegerField(choices=roles,default=2)
    full_name = models.CharField(max_length=50,null=False,blank=False)
    phone = models.CharField(null=False,max_length=30,unique=True)
    # email = models.EmailField(unique=True)

class UserInterestingAnalyz(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    interests = models.TextField(blank=True)

class UserActionTimeSetAd(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    last_active = models.DateTimeField(null=True, blank=True)
    session_duration = models.IntegerField(default=0)
