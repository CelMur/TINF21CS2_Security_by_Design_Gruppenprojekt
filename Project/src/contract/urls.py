# urls.py
from django.urls import path
from .views import CustomerInfoView

app_name = 'contract'  # Replace with your app name

urlpatterns = [
    path("", CustomerInfoView.as_view(), name='contract_form'),

]
