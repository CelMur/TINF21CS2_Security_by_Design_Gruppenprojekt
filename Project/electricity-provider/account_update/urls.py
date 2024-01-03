from django.urls import path
from .views import UserUpdateView

urlpatterns = [
    path('', UserUpdateView.as_view(), name='update_profile'),
]