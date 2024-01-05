from django.urls import path
from .views import BankAccountView

urlpatterns = [
    path('', BankAccountView.as_view(), name='bank_account'),
]
