from datetime import datetime, timedelta
import json
import random
from typing import Any
import uuid
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from measurement_point.models import MeasurementPoint
from contract.models import Contract

from utils.measurement_api import Api

from utils.logger import *

class UiCustomerPage(LoginRequiredMixin, TemplateView):
    login_url = '/login/'  # Redirect URL if user is not authenticated
    template_name =  "ui_customer_page.html"

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.__api = Api.get_instance()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        contracts = Contract.objects.filter(user=self.request.user, is_active=True)

        logger.info(len(contracts))

        now = datetime.now()
        start_time_month = datetime(now.year, now.month, 1)
        end_time_month = now

        

        start_time_today = datetime(now.year, now.month, now.day)
        end_time_today = now

        for contract in contracts:
            current_readings = {}

            current_readings['month'] = json.dumps(
                self.__api.get_meter_measurements(
                    contract.measurement_point.meter_uid,
                    start_time=start_time_month,
                    end_time=end_time_month,
                    data_interval= 60 * 60 * 12
                )
            )
            current_readings['day'] = json.dumps(
                self.__api.get_meter_measurements(
                    contract.measurement_point.meter_uid,
                    start_time=start_time_today,
                    end_time=end_time_today,
                    data_interval= 60 * 15
                )
            )
            # this is nessary because the current_readings are sharedfor some reason. 
            # creating a new dict for each contract fixes this Problem
            contract.measurement_point.current_readings = current_readings
       
        context['contracts'] = contracts
        return context
    
    def generate_mock_messwerte(self, num_values=100):
        base_time = datetime(2023, 10, 12, 4, 0, 0)
        base_value = 1200.205

        mock_messwerte = []
        for i in range(num_values):
            timestamp = base_time + timedelta(seconds=i*500)
            value = base_value + i *10
            mock_messwerte.append({
                "timestamp": timestamp.isoformat() + "+00:00",
                "value": round(value, 3)
            })

        return mock_messwerte

    