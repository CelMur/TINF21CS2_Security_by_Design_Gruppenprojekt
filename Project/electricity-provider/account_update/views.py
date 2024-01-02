from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from utils.logger import *

User = get_user_model()

class UserUpdateView(generics.UpdateAPIView):
    
    permission_classes = [IsAuthenticated]

    _logger = logging.getLogger(__name__)

    def post(self, request, *args, **kwargs):
        user = self.request.user

        password = request.data.get('verify_password')
        if not password or not authenticate(username=user.username, password=password):
            return Response({"error": "Password is required to update profile."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            serializer = self.get_serializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
                
        except Exception as e:
            self._logger.error(e, exc_info=True)
            return Response({"error": "Failed to update profile."}, status=status.HTTP_400_BAD_REQUEST)
