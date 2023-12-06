from django.shortcuts import render
from django.views import View
from .forms import CustomerInfoForm

class CustomerInfoView(View):
    def contract_form_standard(request):
        return render(request, 'contract_form_standard.html')
    def contract_form_premium(request):
        return render(request, 'contract_form_premium.html')
    def contract_form_green(request):
        return render(request, 'contract_form_green.html')
    
    