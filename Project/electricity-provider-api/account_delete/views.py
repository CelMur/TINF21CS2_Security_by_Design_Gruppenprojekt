from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    lookup_field = 'id'  # or 'username' if you want to lookup by username

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
