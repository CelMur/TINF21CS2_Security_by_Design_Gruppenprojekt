from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class OverviewView(View):
    def get(self, request):
        return render(request, 'overview.html')

@method_decorator(login_required, name='dispatch')
class ChangeTariffView(View):
    def get(self, request):
        # Fetch user's contracts
        contracts = Contract.objects.filter(user=request.user)
        return render(request, 'change_data_overview.html', {'contracts': contracts})

    def post(self, request):
        # Process form submission, update contract values, and authenticate user
        # ...

        return redirect('overview')  # Redirect to the overview page after submission

class ChangePersonalDataView(View):
    # Similar structure as ChangeTariffView
    pass

class ChangeBillingInfoView(View):
    # Similar structure as ChangeTariffView
    pass

class ReportIssueView(View):
    # Similar structure as ChangeTariffView
    pass
