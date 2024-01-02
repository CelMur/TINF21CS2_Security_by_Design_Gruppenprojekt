from django.urls import path
from .views import UserAuthenticationView

urlpatterns = [
    path('', UserAuthenticationView.as_view(), name='register'),
]
