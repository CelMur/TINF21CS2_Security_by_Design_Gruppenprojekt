from datetime import datetime
import uuid
from django.conf import settings
from django.db import models

# Create your models here.
class Contract(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.ForeignKey('address.Address', on_delete=models.CASCADE, related_name='address')
    billing_address = models.ForeignKey('address.Address', on_delete=models.CASCADE, related_name='billing_address')
    bank_account = models.ForeignKey('bank_account.BankAccount', on_delete=models.CASCADE)
    measurement_point = models.OneToOneField('measurement_point.MeasurementPoint', on_delete=models.CASCADE, related_name='contract',null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tariff = models.ForeignKey('energy_tariff.EnergyTariff', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    # is_verified
    

    class Meta:
        db_table = "contract"


    @property
    def latest_reading(self):
        if self.measurement_point is None: return 0
        if self.measurement_point.latest_reading is None: return 0

        return self.measurement_point.latest_reading
    
    @property
    def current_costs(self):
        return self.latest_reading * self.price
    
    @property
    def current_month(self):
        return datetime.now().month
    
    @property
    def current_month_name(self):
        return datetime.now().strftime("%B")