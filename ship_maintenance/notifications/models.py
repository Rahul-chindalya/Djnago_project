from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):

    type_choice = [
        ('JOB_CREATED','JOB_CREATED'),
        ('JOB_UPDATED','JOB_UPDATED'),
        ('JOB_COMPLETED','JOB_COMPLETED'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="notifications")
    message = models.TextField()
    notification_type = models.CharField(max_length=50,choices=type_choice)
    is_ready = models.BooleanField(default=False)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - ({self.notification_type})"