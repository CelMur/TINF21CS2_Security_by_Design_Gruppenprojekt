from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from energy_tariff.models import EnergyTariff
from contract.models import Contract

class UiContractPage(LoginRequiredMixin, TemplateView):
    login_url = '/login/'  # Redirect URL if user is not authenticated
    template_name =  "ui_contract_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['contracts'] = Contract.objects.filter(user=self.request.user, is_active=True)
        context['failed_login_attempts'] = self.request.user.failed_login_attempts

        return context
    

class UiNewContractPage(LoginRequiredMixin, TemplateView):
    login_url = '/login/'  # Redirect URL if user is not authenticated
    template_name =  "ui_new_contract_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tariffs'] = EnergyTariff.objects.all()

        # You can add any additional context data here

        return context