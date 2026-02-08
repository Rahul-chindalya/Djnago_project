from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    discount = models.IntegerField()
    available_quantity = models.IntegerField()
    image = models.ImageField(upload_to='product/',null=True,blank=True)

    def __str__(self):
        return self.name 