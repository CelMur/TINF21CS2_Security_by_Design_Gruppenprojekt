from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import EnergyTariff
from .serializers import EnergyTariffSerializer

# Create your views here.
class EnergyTariffView(ListCreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = EnergyTariffSerializer
    queryset = EnergyTariff.objects.all()
    
    # Tariffs are public, so no need to filter by user
    # DISCLAIMER:Tariffs will not be created by the API, we assume they will be created elsewhere and then imported