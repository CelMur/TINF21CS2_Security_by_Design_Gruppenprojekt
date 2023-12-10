
import uuid
from rest_framework import serializers
from address.models import Address

from .models import MeasurementPoint

class MeasurementPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementPoint
        fields = ('meter_uid', 'address', 'is_active', 'household_size','latest_reading', 'latest_reading_date', 'created_at')
        read_only_fields = ('meter_uid', 'created_at', 'latest_reading_date')


    def validate_address(self, value):
        '''
        Validates the address field.
        The address field can be either a reference to an existing address or a dictionary containing the address data.

        Args:
            value (int or dict): The value of the address field.

        Returns:
            Address: The validated address object.

        Raises:
            ValidationError: If the address field is invalid.
        Raises:
            Exception: If any other error occurs (=> probably a bug in the code, rofl >_<)

        '''
        address = None
        if isinstance(value, serializers.UUIDField):
            # Handle address reference
            address = Address.objects.filter(id=value).first()
            if address is None:
                raise serializers.ValidationError("Invalid address reference.")
        elif isinstance(value, dict):
            # Handle address data
            #TODO: this should be handled by the AddressSerializer
            if 'street' not in value or 'city' not in value or 'street_number' not in value:
                raise serializers.ValidationError("Invalid address data. Missing required fields.")
            else:
                address = Address.objects.create(**value)
        else:
            raise serializers.ValidationError("Invalid address format.")
        return address

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
        