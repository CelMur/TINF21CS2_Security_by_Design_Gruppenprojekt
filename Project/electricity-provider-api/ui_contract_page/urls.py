from django.urls import path
from .views import UiContractPage

urlpatterns = [
    path('contract/', UiContractPage.as_view(), name='ui_contract_page'),
]