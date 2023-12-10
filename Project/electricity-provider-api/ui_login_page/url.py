from django.urls import path
from .views import UiLoginPage

urlpatterns = [
    path('', UiLoginPage.as_view(), name='ui_login_page'),
]