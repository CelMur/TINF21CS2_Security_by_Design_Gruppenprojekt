from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerInfoForm

class CustomerInfoView(View):
    template_name = "contract_form.html"

    def get(self, request):
        form = CustomerInfoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomerInfoForm(request.POST)
        if form.is_valid():
            customer_info = form.save(commit=False)
            customer_info.user = request.user  # Assign the logged-in user
            customer_info.save()
            return redirect('success_page')  # Change to your success page URL

        return render(request, self.template_name, {'form': form})
