from django.urls import path
from .views import ActivateAccountView

urlpatterns = [
    path('activate/<token>/<second_token>/', ActivateAccountView.as_view(), name='activate'),
    # path('confirm/<uidb64>/<token>/>', ActivateAccountView.as_view(), name='confirm'),
]


