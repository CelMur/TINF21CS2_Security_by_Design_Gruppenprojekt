from django.urls import path
from .views import RegisterPageView
app_name = "Register"

urlpatterns = [
    path("", RegisterPageView.as_view() , name="register"),
]