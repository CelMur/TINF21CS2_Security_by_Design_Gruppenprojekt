from datetime import datetime
import uuid
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from utils.measurement_api import Api
from django.db.transaction import TransactionManagementError
from django.db import transaction

from utils.logger import *

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



class MeasurementReading(models.Model):
    measurement_point = models.ForeignKey('MeasurementPoint', on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    first_reading = models.DecimalField(max_digits=10, decimal_places=2)
    last_reading = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.IntegerField(editable=False)
    year = models.IntegerField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "measurement_reading"
        unique_together = ('measurement_point','year', 'month')

    def save(self, *args, **kwargs):
        try:
            with transaction.atomic():
                super().save(*args, **kwargs)

                self.measurement_point.last_reading = self.last_reading
                self.measurement_point.latest_reading_date = self.timestamp.date()
                self.measurement_point.save()
        except TransactionManagementError:
            pass
        except Exception as e:
            logger.error(e)
            raise e

    @property
    def meter_uid(self):
        if self.measurement_point is None: return None
        return self.measurement_point.meter_uid


    def __str__(self):
        return f"{self.meter_uid} - {self.year} - {self.month}"
    
    def __repr__(self):
        return f"{self.meter_uid} - {self.year} - {self.month}"



    def __lt__(self, o: object) -> bool:
        if not isinstance(o, MeasurementReading):
            return False
        
        return self.year < o.year and self.month < o.month

    def __gt__(self, o: object) -> bool:
        if not isinstance(o, MeasurementReading):
            return False
        
        return self.year > o.year and self.month > o.month

    def __le__(self, o: object) -> bool:
        if not isinstance(o, MeasurementReading):
            return False
        
        return self.year <= o.year and self.month <= o.month

    def __ge__(self, o: object) -> bool:
        if not isinstance(o, MeasurementReading):
            return False
        
        return self.year >= o.year and self.month >= o.month