from django.urls import path
from .views import ContractView

urlpatterns = [
    path('', ContractView.as_view(), name='contract'),
]
