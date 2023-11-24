from django.urls import path
from .views import SignUpPageView
app_name = "sign_up"

urlpatterns = [
    path("", SignUpPageView.as_view() , name="signup"),
]