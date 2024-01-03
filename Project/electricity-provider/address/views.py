from django.conf import settings
from .models import Address
from .serializers import AddressSerializer, AddressReadSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import TokenAuthentication


# Create your views here.
class AddressView(ListCreateAPIView):

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AddressReadSerializer
        return AddressSerializer

    def get_queryset(self):
        user = self.request.user
        adresses = Address.objects.filter(user=user)
        return adresses

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    