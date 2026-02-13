from django.db import models
from ships.models import Ship
from accounts.models import User
from django.utils import timezone

# Create your models here.
class MaintainenceJobs(models.Model):
    prority_choice = [
        ('LOW','LOW'),
        ('MEDIUM','MEDIUM'),
        ('HIGH','HIGH'),
    ]
    status_choice =[
        ('PENDING','PENDING'),
        ('IN_PROGRESS','IN_PROGRESS'),
        ('COMPLETED','COMPLETED'),
    ]
    ship = models.ForeignKey(Ship,on_delete=models.CASCADE,related_name='jobs')
    job_type = models.CharField(max_length=100)
    prority = models.CharField(max_length=20,choices=prority_choice)
    status = models.CharField(max_length=20,choices=status_choice)
    assigned_engineer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    scheduled_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return f"{self.ship.name} - ({self.job_type})"