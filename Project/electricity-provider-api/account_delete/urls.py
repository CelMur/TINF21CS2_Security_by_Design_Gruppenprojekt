from django.urls import path
from .views import UserDeleteView

urlpatterns = [
    path('', UserDeleteView.as_view(), name='register'),
]