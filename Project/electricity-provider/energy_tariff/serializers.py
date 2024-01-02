from rest_framework import serializers
from .models import EnergyTariff


class EnergyTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyTariff
        fields = '__all__'