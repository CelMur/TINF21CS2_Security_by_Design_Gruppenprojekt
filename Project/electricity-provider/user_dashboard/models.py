from django.db import models
from sign_up.models import CustomUser
class DashboardInfo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    tariff = models.CharField(max_length=100)
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.address}, {self.postal_code}, {self.city}"
