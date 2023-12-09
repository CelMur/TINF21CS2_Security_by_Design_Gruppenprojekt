from django.views.generic import ListView
from .models import Bills

class BillingListView(ListView):
    model = Bills
    template_name = 'billing.html'
    context_object_name = 'bills'
