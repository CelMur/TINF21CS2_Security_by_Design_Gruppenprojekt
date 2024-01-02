from django.urls import path
from .views import UiCustomerPage

urlpatterns = [
    path('customer/', UiCustomerPage.as_view(), name='ui_customer_page'),
]