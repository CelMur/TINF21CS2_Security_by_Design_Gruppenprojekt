from django.urls import path
from .views import PricingPageView
app_name = "Pricing"

urlpatterns = [
    path("", PricingPageView.as_view() , name="pricing"),
    path('premium_plan/', PricingPageView.as_view(template_name='premium_plan.html'), name='premium_plan'),
    path('standard_plan/', PricingPageView.as_view(template_name='standard_plan.html'), name='standard_plan'),
    path('green_plan/', PricingPageView.as_view(template_name='green_plan.html'), name='green_plan'),
]