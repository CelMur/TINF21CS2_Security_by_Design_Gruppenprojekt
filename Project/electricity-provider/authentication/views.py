import hashlib
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.db.models import F
from django.contrib.auth import authenticate, login

from utils.logger import *

from .serializers import UserAuthenticationSerializer

class UserAuthenticationView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        

        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            login(request, user)
            serializer = UserAuthenticationSerializer(instance=user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            if username is not None:
                get_user_model().objects.filter(email=username).update(failed_login_attempts=F('failed_login_attempts') + 1)
                #masking of the username to prevent information leakage in the logs
                hashed_username = hashlib.sha256(username.encode('utf-8')).hexdigest()
                logger.warn(f'failed authentication for user {hashed_username}')
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)