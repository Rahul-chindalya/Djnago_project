from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    role_choice = [
        ('admin','amdin'),
        ('inspector','inspector'),
        ('engineer','engineer'),
    ]
    phone_no = models.BigIntegerField(blank=True,null=True)
    role = models.CharField(max_length=50,choices=role_choice)
    address = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return f"{self.user.username} - ({self.role})"