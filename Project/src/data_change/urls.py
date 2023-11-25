from django.urls import path
from .views import OverviewView, ChangeTariffView, ChangePersonalDataView, ChangeBillingInfoView, ReportIssueView

urlpatterns = [
    path('overview/', OverviewView.as_view(), name='overview'),
    path('change_tariff/', ChangeTariffView.as_view(), name='change_tariff'),
    path('change_personal_data/', ChangePersonalDataView.as_view(), name='change_personal_data'),
    path('change_billing_info/', ChangeBillingInfoView.as_view(), name='change_billing_info'),
    path('report_issue/', ReportIssueView.as_view(), name='report_issue'),
]
