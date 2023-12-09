# contract_viewer/models.py
from django.db import models
from django.contrib.auth.models import User

class Bills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=50)
    object_name = models.CharField(max_length=255)
    month = models.DateField()
    kwh = models.FloatField()
    billing_amount = models.FloatField()
    billing_status = models.CharField(max_length=50)
