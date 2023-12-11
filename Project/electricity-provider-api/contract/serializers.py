from datetime import datetime
from rest_framework import serializers
from .models import Contract

class ContractSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Contract
        fields = ['id', 'start_date', 'end_date', 'user', 'address']
        read_only_fields = ['user', 'address']
    
    def validate_start_date(self, value):
        if value == "":
            raise serializers.ValidationError("Start date cannot be empty")
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise serializers.ValidationError("Start date must be a valid date in the format YYYY-MM-DD")
        return value
    
    def validate_end_date(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise serializers.ValidationError("End date must be a valid date in the format YYYY-MM-DD")
        return value
    
    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        self.validate_start_date(start_date)
        
        if end_date:
            self.validate_end_date(end_date)

        #check if start_date and end_date are both set:
        if start_date and end_date:
            # Convert strings to date objects
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

            if start_date > end_date:
                raise serializers.ValidationError("End date cannot be before start date")
            if start_date == end_date:
                raise serializers.ValidationError("End date cannot be the same as start date")

        return data