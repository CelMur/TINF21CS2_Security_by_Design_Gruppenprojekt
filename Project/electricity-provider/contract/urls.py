# urls.py
from django.urls import path
from .views import CustomerInfoView

app_name = 'contract'

urlpatterns = [
    path("contract_form_standard/", CustomerInfoView.contract_form_standard, name='contract_form_standard'),
    path("contract_form_premium/", CustomerInfoView.contract_form_premium, name='contract_form_premium'),
    path("contract_form_green/", CustomerInfoView.contract_form_green, name='contract_form_green'),
    ]
