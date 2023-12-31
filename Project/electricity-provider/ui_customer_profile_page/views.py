from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class UiCustomerProfilePage(LoginRequiredMixin, TemplateView):
    login_url = '/login/'  # Redirect URL if user is not authenticated
    template_name =  "ui_customer_profile_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # You can add any additional context data here

        return context