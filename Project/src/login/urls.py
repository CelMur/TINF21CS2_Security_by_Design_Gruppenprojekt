from django.urls import path
from .views import LoginPageView
app_name = "login"

urlpatterns = [
    path("", LoginPageView.as_view() , name="login"),
]