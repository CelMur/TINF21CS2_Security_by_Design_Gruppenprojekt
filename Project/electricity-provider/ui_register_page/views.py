from django.views.generic import TemplateView
from django.shortcuts import redirect
# Create your views here.

class UiRegisterPage(TemplateView):
    template_name =  "ui_register_page.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # You can add any additional context data here

        return context