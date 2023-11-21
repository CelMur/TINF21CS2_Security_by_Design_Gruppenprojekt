from django.views.generic import TemplateView


# Create your views here.
class LoginPageView(TemplateView):
    template_name =  "Login.html"
