from django.urls import path
from .views import LogoutPageView
from django.contrib.auth import views as auth_views
app_name = "logout"

urlpatterns = [
    path('', LogoutPageView, name='logout'),
]
