from django.urls import path
from .views import UiMainPage

urlpatterns = [
    path('', UiMainPage.as_view(), name='ui_main_page'),
]