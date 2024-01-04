from django.urls import path
from .views import ContractView, ContractViewCancel

urlpatterns = [
    path('', ContractView.as_view(), name='contract'),
    path('cancel/', ContractViewCancel.as_view(), name='contract'),
]
