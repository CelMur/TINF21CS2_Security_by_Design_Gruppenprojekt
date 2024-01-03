
import uuid
from rest_framework import serializers
from .models import Address
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'street_number', 'postal_code', 'city', 'user']
        read_only_fields = ['user', 'id']


    def validate_street(self, value):
        if value == "":
            raise serializers.ValidationError("Street cannot be empty")
        return value
    
    def validate_street_number(self, value):
        if value == "":
            raise serializers.ValidationError("Street number cannot be empty")
        return value
    
    def validate_postal_code(self, value):
        if value == "":
            raise serializers.ValidationError("Postal code cannot be empty")
        return value
    
    def validate_city(self, value):
        if value == "":
            raise serializers.ValidationError("City cannot be empty")
        return value

    def create(self, validated_data):
        """
        Return the existing address for the user if it exists, otherwise create a new one.
        """
        user = self.context['request'].user
        validated_data.pop('user', None)
        address, created = Address.objects.get_or_create(user=user, **validated_data)
        return address
        
    # def create_or_retrieve_address(self, data):
    #     """
    #     Try to interpret the data as a UUID and retrieve the corresponding address.
    #     If the data is not a valid UUID or no such address exists, try to create an address from the data.
    #     """
    #     user = self.context['request'].user
    #     try:
    #         # Try to interpret the data as a UUID
    #         address_uuid = uuid.UUID(data)
    #         # Try to retrieve the address with the given UUID
    #         return user.address_set.get(id=address_uuid)
    #     except (ValueError, ObjectDoesNotExist):
    #         # If the data is not a valid UUID or no such address exists,
    #         # try to create an address from the data
    #         serializer = AddressSerializer(data=data, context={'request': self.context['request']})
    #         if serializer.is_valid(raise_exception=True):
    #             return serializer.save()