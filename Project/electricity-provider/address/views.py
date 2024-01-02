from django.conf import settings
from .models import Address
from .serializers import AddressSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import TokenAuthentication


# Create your views here.
class AddressView(ListCreateAPIView):

    if settings.DEBUG:
        authentication_classes = [TokenAuthentication]
    else:
        authentication_classes = [SessionAuthentication]

    permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializer

    queryset = Address.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Address.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
