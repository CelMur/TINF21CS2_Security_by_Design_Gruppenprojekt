from datetime import date
import uuid
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class UiCustomerPage(LoginRequiredMixin, TemplateView):
    login_url = '/login/'  # Redirect URL if user is not authenticated
    template_name =  "ui_customer_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add mock contracts to context
        context['contracts'] = self.generate_mock_contracts(10)

        return context
    
    def generate_mock_contracts(self, num_contracts):
        mock_contracts = []
        for i in range(num_contracts):
            mock_contracts.append({
                'id': uuid.uuid4(),
                'user': i,
                'address': uuid.uuid4(),
                'billing_address': uuid.uuid4(),
                'bank_account': uuid.uuid4(),
                'measurement_point': uuid.uuid4(),
                'start_date': date.today(),
                'end_date': date.today(),
                'price': 100.00,
                'tariff': uuid.uuid4(),
                'is_active': True
            })
        return mock_contracts