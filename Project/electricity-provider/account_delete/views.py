from django.conf import settings
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

User = get_user_model()

class UserDeleteView(generics.DestroyAPIView):
   
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

