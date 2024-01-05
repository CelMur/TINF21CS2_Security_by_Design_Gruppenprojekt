from datetime import datetime, timedelta
import json
import uuid
from django.conf import settings
from django.db import models
from utils.measurement_api import Api
from utils.logger import *

from django.db import transaction

from measurement_point.models import MeasurementReading

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__api = Api.get_instance()
    

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
    def current_month_costs(self):
        return self.current_month_consumption * self.price
    
    @property
    def current_month(self):
        return datetime.now().month
    
    @property
    def current_year(self):
        return datetime.now().year
    
    @property
    def current_month_name(self):
        return datetime.now().strftime("%B")
    
    @property
    def current_month_consumption(self):
        if self.measurement_point is None: return 0
        
        reading = MeasurementReading.objects.filter(measurement_point_id=self.measurement_point.meter_uid, month=self.current_month, year=self.current_year)
        if reading:
            reading = reading.first()
            return reading.last_reading - reading.first_reading
        else:
            return 0
        

    def update_current_month_consumption(self):
        try:
            with transaction.atomic():
                now = datetime.now()
                current_month = now.month
                current_year = now.year

                if self.is_active == False: return
                if self.measurement_point is None: return
                
                meter_uid = self.measurement_point.meter_uid

                reading = MeasurementReading.objects.filter(measurement_point_id=meter_uid, year=current_year, month=current_month)
                
                # Case 1: There exists a reading for the current month -> update
                # Case 2: There is no reading for the current month -> create
                # Case 3: Ther are no readings at all -> create
                if reading.exists():
                    # Case 1
                    #update reading
                    new_reading_value = self.__api.get_meter_measurements(meter_uid, now - timedelta(seconds=60), now, 1)
                    new_reading_value = new_reading_value['data']

                    if len(new_reading_value) == 0: 
                        new_reading_value = 0
                    else:
                        value = 0
                        # get first value for list not none
                        for v in new_reading_value:
                            if v['value'] is not None:
                                value = v['value']
                                break
                        reading.update(last_reading=value, timestamp=now)

        except Exception as e:
            logger.error(e, exc_info=True)
            raise e