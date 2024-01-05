from django.urls import path
from .views import UiContractPage, UiNewContractPage

urlpatterns = [
    path('contract/', UiContractPage.as_view(), name='ui_contract_page'),
    path('contract/new/', UiNewContractPage.as_view(), name='ui_new_contract_page'),
]