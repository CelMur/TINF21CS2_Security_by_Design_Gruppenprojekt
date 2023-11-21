from django.urls import path
from .views import LandingPageView
app_name = "LandingPage"

urlpatterns = [
    path("", LandingPageView.as_view() , name="index"),
]