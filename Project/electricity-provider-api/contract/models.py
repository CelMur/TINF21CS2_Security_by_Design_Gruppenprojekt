import uuid
from django.conf import settings
from django.db import models

# Create your models here.
class Contract(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.ForeignKey('address.Address', on_delete=models.CASCADE)
    billing_address = models.ForeignKey('address.Address', on_delete=models.CASCADE, related_name='billing_address')
    bank_account = models.ForeignKey('bank_account.BankAccount', on_delete=models.CASCADE)
    measurement_point = models.OneToOneField('measurement_point.MeasurementPoint', on_delete=models.CASCADE, related_name='contract',null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tariff = models.ForeignKey('energy_tariff.EnergyTariff', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    

    class Meta:
        db_table = "contract"