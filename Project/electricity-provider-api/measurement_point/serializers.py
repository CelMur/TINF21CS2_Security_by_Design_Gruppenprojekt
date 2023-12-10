
from rest_framework import serializers
from .models import MeasurementPoint

class MeasurementPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementPoint
        fields = ('id', 'name', 'address', 'city', 'country', 'zip_code', 'latitude', 'longitude', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')