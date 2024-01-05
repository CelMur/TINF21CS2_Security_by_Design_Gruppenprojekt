from rest_framework import serializers
from .models import EnergyTariff

from utils.logger import *
class EnergyTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyTariff
        fields = '__all__'
