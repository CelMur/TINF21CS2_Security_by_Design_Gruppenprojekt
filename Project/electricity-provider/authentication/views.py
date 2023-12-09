from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserAuthenticationSerializer
from utils.logger import *

class UserAuthenticationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        #TODO:needs sanitization
        username = request.data.get('username')
        password = request.data.get('password')
        

        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            response_data = {'token': token.key}
            serializer = UserAuthenticationSerializer(instance=user)
            response_data.update(serializer.data)
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            logger.critical(f'failed authentication for user {username}')
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)