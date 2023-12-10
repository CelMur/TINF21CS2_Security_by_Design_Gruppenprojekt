from django.urls import path
from .views import UiCustomerProfilePage

urlpatterns = [
    path('profile/', UiCustomerProfilePage.as_view(), name='ui_customer_profile_page'),
]