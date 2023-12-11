from django.urls import path
from .views import UiPricingPage

urlpatterns = [
    path('pricing/', UiPricingPage.as_view(), name='ui_pricing_page'),
]