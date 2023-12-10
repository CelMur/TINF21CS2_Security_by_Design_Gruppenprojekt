# authentication/serializers.py
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User

class UserAuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']  
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserAuthenticationSerializer, self).create(validated_data)