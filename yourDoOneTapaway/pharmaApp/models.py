from django.db import models
from django.contrib.auth.models import User
from AcoountApp.models import PharmacyProfile,UserProfile

# Create your models here.

class PharmacyAddProduct(models.Model):
    productId = models.BigAutoField(primary_key=True)
    user = models.ManyToManyField(PharmacyProfile)
    name =  models.CharField(max_length=100)
    image = models.ImageField(upload_to="static")
    description  = models.TextField(max_length=500)
    Quantity = models.IntegerField()
    Price  = models.IntegerField()
    Dom = models.DateField()
    Doe = models.DateField()

    def __str__(self):
        return self.name
