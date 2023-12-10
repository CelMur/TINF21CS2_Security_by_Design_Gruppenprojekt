from django.urls import path
from .views import UiLoginPage

urlpatterns = [
    path('', UiCustomerProfilePage.as_view(), name='ui_customer_profile_page'),
]