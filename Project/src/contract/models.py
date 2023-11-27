# models.py
from django.db import models
from sign_up.models import CustomUser

class CustomerInfo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #Orientiert sich an system generierter User Nummer
    meter_number = models.CharField(max_length=50)
    street = models.CharField(max_length=255)
    town = models.CharField(max_length=100)
    postal_number = models.CharField(max_length=20)
    terms_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Information"
