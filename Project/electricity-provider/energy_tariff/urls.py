from django.urls import path
from .views import EnergyTariffView

urlpatterns = [
    path('', EnergyTariffView.as_view(), name='energy_tariff'),
]
