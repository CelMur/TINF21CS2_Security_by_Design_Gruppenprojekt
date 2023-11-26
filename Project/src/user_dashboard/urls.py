# project/urls.py
from django.urls import path, include
app_name = "dashboard"

urlpatterns = [
    path('user_dashboard/', include('user_dashboard.urls')),
]
