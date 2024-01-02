from django.db import models

# Create your models here.
class MeasurementPoint(models.Model):
    
    meter_uid = models.CharField(max_length=255, unique=True, editable=False)
    address = models.ForeignKey('address.Address', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    latest_reading = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    latest_reading_date = models.DateField(null=True, blank=True)
    household_size = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "measurement_point"
        
