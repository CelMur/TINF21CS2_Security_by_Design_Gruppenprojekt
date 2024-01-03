import uuid
from django.db import models

# Create your models here.
class EnergyTariff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=45, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    renewable = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "energy_tariff"
        ordering = ["-created_at"]
    def __str__(self):
        return self.name