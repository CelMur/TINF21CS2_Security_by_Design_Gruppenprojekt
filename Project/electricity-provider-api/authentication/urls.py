from django.urls import path
from .views import UserAuthenticationView

urlpatterns = [
    path('auth/', UserAuthenticationView.as_view(), name='register'),
]
