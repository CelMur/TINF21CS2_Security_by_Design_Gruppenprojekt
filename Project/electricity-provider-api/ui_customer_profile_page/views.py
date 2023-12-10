from django.views.generic import TemplateView

# Create your views here.

class UiCustomerProfilePage(TemplateView):
    template_name =  "ui_customer_profile_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # You can add any additional context data here

        return context