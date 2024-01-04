from datetime import date
import datetime
import random
import uuid
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class UiCustomerPage(LoginRequiredMixin, TemplateView):
    login_url = '/login/'  # Redirect URL if user is not authenticated
    template_name =  "ui_customer_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add mock contracts to context
        context['messwerte'] = self.generate_mock_messwerte()

        return context
    
    def generate_mock_messwerte(self, num_values=100):
        base_time = datetime.datetime(2023, 10, 12, 4, 0, 0)
        base_value = 1200.205

        mock_messwerte = []
        for i in range(num_values):
            timestamp = base_time + datetime.timedelta(seconds=i*500)
            value = base_value + i *10
            mock_messwerte.append({
                "timestamp": timestamp.isoformat() + "+00:00",
                "value": round(value, 3)
            })

        return mock_messwerte

    