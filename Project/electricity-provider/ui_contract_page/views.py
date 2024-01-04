from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from energy_tariff.models import EnergyTariff

class UiContractPage(LoginRequiredMixin, TemplateView):
    login_url = '/login/'  # Redirect URL if user is not authenticated
    template_name =  "ui_contract_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # You can add any additional context data here

        return context
    

class UiNewContractPage(LoginRequiredMixin, TemplateView):
    login_url = '/login/'  # Redirect URL if user is not authenticated
    template_name =  "ui_new_contract_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tariffs'] = EnergyTariff.objects.all()

        # You can add any additional context data here

        return context