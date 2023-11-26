# project/urls.py
from django.urls import path, include
from .views import UserDashboardView
app_name = "dashboard"

urlpatterns = [
    path("", UserDashboardView.as_view(), name = "dashboard"),
]
