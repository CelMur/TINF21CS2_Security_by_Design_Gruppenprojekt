
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Contract


@method_decorator(login_required, name='dispatch')
class UserDashboardView(View):
    template_name = 'user_dashboard.html'

    def get(self, request):
        # Fetch user's contracts
        contracts = Contract.objects.filter(user=request.user)
        return render(request, self.template_name, {'contracts': contracts})
