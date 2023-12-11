from django.urls import path
from .views import UiRegisterPage

urlpatterns = [
    path('register/', UiRegisterPage.as_view(), name='ui_register_page'),
]