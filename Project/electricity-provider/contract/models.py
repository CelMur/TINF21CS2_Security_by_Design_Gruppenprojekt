# models.py
from django.db import models
from sign_up.models import CustomUser

class Contract(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #Orientiert sich an system generierter User Nummer
    meter_uid = models.CharField(max_length=50)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_number = models.CharField(max_length=20)
    iban = models.CharField(max_length=20)
    debit_checked = models.BooleanField(default=False)
    terms_confirmed = models.BooleanField(default=False)
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2)

    

    def __str__(self):
        return f"{self.user.username}'s Information"
