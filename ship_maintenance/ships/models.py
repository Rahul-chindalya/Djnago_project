from django.db import models

# Create your models here.
class Ship(models.Model):
    status_choice = [
        ('Active','Active'),
        ('Maintenance','Maintenance'),
        ('Docked','Docked')
    ]
    name = models.CharField(max_length=50)
    imo_number = models.CharField(max_length=50)
    flag = models.CharField(max_length=50)
    status = models.CharField(max_length=50,choices=status_choice)

    def __str__(self):
        return self.name