from django.db import models
from django.contrib.auth.models import AbstractUser
from common.choose import UserChoices,DegreeOwner
from .manager import AccountManager 

# Create your models here.

class Account(AbstractUser):
    user=models.CharField(max_length=10,choices=UserChoices.choices,default=UserChoices.STAFF)
    is_active=models.BooleanField(default=False)
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=50,null=True,blank=True)
    degree=models.CharField(max_length=50,null=True,blank=True)
    
    EMAIL_FIELD = "password"
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email']

    objects=AccountManager()


    def __str__(self):
        return str(self.username)
    
    
    class Meta:
        verbose_name='Account'
        verbose_name_plural='Accounts'



        
    
    
    
