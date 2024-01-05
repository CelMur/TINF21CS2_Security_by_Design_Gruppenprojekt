
import django.db.transaction as transcaction
from rest_framework import serializers
from rest_framework.fields import empty
from address.models import Address
from utils.measurement_api import Api

import django.db.transaction as trancaction

from address.serializers import AddressSerializer

from .models import MeasurementPoint
from django.core.exceptions import ObjectDoesNotExist

from utils.logger import *

class MeasurementPointSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = MeasurementPoint
        fields = ('meter_uid', 'address', 'is_active', 'household_size','latest_reading', 'latest_reading_date', 'created_at')
        read_only_fields = ('meter_uid', 'created_at')

    

    def validate_household_size(self, value):
        '''
        Checks if the household size is valid. 300 >= household_size > 0

        Args:
            value (int): The value of the household_size field.

        Returns:
            int: The validated household_size.

        Raises:
            ValidationError: If the household_size is invalid.
        Raises:
            Exception: If any other error occurs (=> probably a bug in the code, !..!)
        '''
        if value < 0:
            raise serializers.ValidationError("Household size must be a positive integer or 0.")
        if value > 300:
            raise serializers.ValidationError("Household size cannot exceed 300.")
        return value
    
    @transcaction.atomic
    def create(self, validated_data):
        
        user = self.context['request'].user
        address_data = validated_data.pop('address')
        meter_uid = validated_data.pop('meter_uid')
        address, _ = Address.objects.get_or_create(user=user,**address_data)

        measurement_point = MeasurementPoint.objects.create(
            meter_uid=meter_uid,
            address=address, 
            **validated_data
        )
        return measurement_point
