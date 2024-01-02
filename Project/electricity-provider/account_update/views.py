from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model, authenticate
from authentication.serializers import UserAuthenticationSerializer
from utils.logger import *

User = get_user_model()

class UserUpdateView(generics.UpdateAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = UserAuthenticationSerializer
    User = get_user_model()

    _logger = logging.getLogger(__name__)

    def patch(self, request, *args, **kwargs):
        user = self.request.user

        password = request.data.get('confirmation_password')
        if not password or not authenticate(username=user.get_username(), password=password):
            return Response({"error": "Password is required to update profile."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            serializer = self.serializer_class(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
                
        except Exception as e:
            self._logger.error(e, exc_info=True)
            return Response({"error": "Failed to update profile."}, status=status.HTTP_400_BAD_REQUEST)
        


