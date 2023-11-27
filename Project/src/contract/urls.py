# urls.py
from django.urls import path
from .views import CustomerInfoView

app_name = 'contract'

urlpatterns = [
    path('contract_form_standard/', CustomerInfoView.as_view(template_name='contract_form_standard.html'), name='contract_form_standard'),
    path("contract_form_premium/", CustomerInfoView.as_view(template_name='contract_form_premium.html'), name='contract_form_premium'),
    path("contract_form_green/", CustomerInfoView.as_view(template_name='contract_form_green.html'), name='contract_form_green'),
    ]
