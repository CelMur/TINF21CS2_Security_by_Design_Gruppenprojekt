# project/urls.py
from django.urls import path, include
from .views import UserDashboardView
app_name = "user_dashboard"

urlpatterns = [
    path("dashboard/", UserDashboardView.as_view(), name = "user_dashboard"),
]
