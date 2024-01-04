
from datetime import datetime
from django.conf import settings
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from energy_tariff.models import EnergyTariff
from address.models import Address
from bank_account.models import BankAccount
from .models import Contract

from measurement_point.views import CreateMeasurementPointView
from .serializers import ContractSerializerForCreate

from utils.logger import *


# Create your views here.
class ContractView(ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ContractSerializerForCreate

    def get_queryset(self):
        user = self.request.user
        return Contract.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)