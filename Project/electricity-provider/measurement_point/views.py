from typing import Any

from django.conf import settings
from utils.measurement_api import Api
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MeasurementPoint
from .serializers import MeasurementPointSerializer
from address.models import Address
import requests

from utils.logger import *
from rest_framework.permissions import IsAuthenticated


class CreateMeasurementPointView(APIView):

    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.__api = Api.get_Api()


    def post(self, request):
        meter_uid = None
        try:
            meter_uid = self.__api.create_meter()
            measurement_point_serializer = MeasurementPointSerializer(data=request.data)
            measurement_point_serializer.is_valid(raise_exception=True)
            measurement_point_serializer.save(meter_uid=meter_uid)
            return Response(measurement_point_serializer.data)
            
        except Exception as e:
            if meter_uid:
                self.__api.delete_meter(meter_uid)
            raise e
class UpdateMeasurementPointView(APIView):
    def get(self, request, meter_uid):
        measurement_point = MeasurementPoint.objects.get(meter_uid=meter_uid)
        # Call the external API to get the latest reading
        response = requests.get('https://external-api.com/endpoint', params={'meter_uid': meter_uid})
        data = response.json()
        # Update the latest_reading and latest_reading_date fields
        measurement_point.latest_reading = data['latest_reading']
        measurement_point.latest_reading_date = data['latest_reading_date']
        measurement_point.save()
        serializer = MeasurementPointSerializer(measurement_point)
        return Response(serializer.data)

class GetMeasurementDataView(APIView):
    def get(self, request, meter_uid):
        # Call the external API to get the measurement data
        response = requests.get('https://external-api.com/endpoint', params={'meter_uid': meter_uid})
        data = response.json()
        # Process the data as needed
        processed_data = self.process_data(data)
        return Response(processed_data)
    

    def process_data(data):
        # not yet sure what to do here xD
        return data