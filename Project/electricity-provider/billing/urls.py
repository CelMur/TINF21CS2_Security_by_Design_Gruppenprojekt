from django.urls import path
from .views import BillingListView

app_name = 'billing'

urlpatterns = [
    path('billing/', BillingListView.as_view(), name='billing_list'),
]