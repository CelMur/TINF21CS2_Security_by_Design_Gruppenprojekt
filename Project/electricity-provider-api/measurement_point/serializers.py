
from rest_framework import serializers
from .models import MeasurementPoint

class MeasurementPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementPoint
        fields = ('meter_uid', 'address', 'is_active', 'latest_reading', 'latest_reading_date', 'created_at')
        read_only_fields = ('meter_uid', 'created_at', 'latest_reading_date')