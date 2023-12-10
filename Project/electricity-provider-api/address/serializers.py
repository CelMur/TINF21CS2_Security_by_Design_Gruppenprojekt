
from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'street_number', 'postal_code', 'city', 'user']
        read_only_fields = ['user']


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
    