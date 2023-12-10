from rest_framework.authtoken.models import Token
import logging
from .serializers import UserRegistrationSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth import get_user_model


# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        #Hashing the password before saving the user
        serializer.save(password=serializer.validated_data['password'])