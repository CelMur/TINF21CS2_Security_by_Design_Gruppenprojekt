from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login

from utils.logger import *

from .models import User
from .serializers import UserAuthenticationSerializer

class UserAuthenticationView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        #TODO:needs sanitization
        username = request.data.get('username')
        password = request.data.get('password')
        

        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            login(request, user)
            serializer = UserAuthenticationSerializer(instance=user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            logger.critical(f'failed authentication for user {username}')
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)