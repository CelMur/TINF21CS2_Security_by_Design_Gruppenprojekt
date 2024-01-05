# authentication/serializers.py
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User

class UserAuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'failed_login_attempts']  
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['failed_login_attempts']
        
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserAuthenticationSerializer, self).create(validated_data)


    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        return super(UserAuthenticationSerializer, self).update(instance, validated_data)