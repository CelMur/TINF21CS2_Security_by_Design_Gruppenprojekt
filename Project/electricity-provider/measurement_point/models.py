from datetime import datetime
import uuid
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from utils.measurement_api import Api
from django.db.transaction import TransactionManagementError

# Create your models here.
class MeasurementPoint(models.Model):
    meter_uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.ForeignKey('address.Address', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    latest_reading = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    latest_reading_date = models.DateField(null=True, blank=True)
    household_size = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # non persistent fields
    current_readings = {}


    class Meta:
        db_table = "measurement_point"
        
@receiver(pre_delete, sender=MeasurementPoint)
def measurement_point_pre_delete(sender, instance, **kwargs):
    api = Api.get_instance()
    api.delete_meter(instance.meter_uid)
