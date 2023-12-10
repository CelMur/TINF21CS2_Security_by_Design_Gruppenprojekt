from django.urls import path
from .views import UiMainPage

urlpatterns = [
    path('', UiRegisterPage.as_view(), name='ui_register_page'),
]