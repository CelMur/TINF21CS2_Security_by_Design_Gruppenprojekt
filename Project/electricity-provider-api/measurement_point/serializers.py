
import django.db.transaction as trancaction
from django.conf import settings
from rest_framework import serializers
from rest_framework.fields import empty
from address.models import Address
from utils.measurement_api import Api

from address.serializers import AddressSerializer

from .models import MeasurementPoint
from django.core.exceptions import ObjectDoesNotExist

class MeasurementPointSerializer(serializers.ModelSerializer):

    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        self.__api = Api(settings.MEASUREMENT_API_KEY, 
                         settings.MEASUREMENT_CUSTOMER_UID, 
                         settings.MEASUREMENT_API_URL)

    class Meta:
        model = MeasurementPoint
        fields = ('meter_uid', 'address', 'is_active', 'household_size','latest_reading', 'latest_reading_date', 'created_at')
        read_only_fields = ('meter_uid', 'created_at', 'latest_reading_date')

    

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
        if value <= 0:
            raise serializers.ValidationError("Household size must be a positive integer.")
        if value > 300:
            raise serializers.ValidationError("Household size cannot exceed 300.")
        return value
    
    
    @trancaction.atomic
    def create(self, validated_data):
        """
        Return the existing measurement point for the user if it exists, otherwise create a new one.
        """

        user = self.context['request'].user

        # Create address if needed
        address_data = validated_data.pop('address', None)
        if address_data:
            address, created = Address.objects.get_or_create(user=user, **address_data)
            validated_data['address'] = address

        # Create meterUID
        meter_uid_data = self.__api.create_meter()

        try:
            return user.measurementpoint
        except ObjectDoesNotExist:
            return super().create(validated_data)