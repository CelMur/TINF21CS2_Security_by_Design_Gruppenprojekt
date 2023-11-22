
from django.forms import inlineformset_factory
from django.http import HttpResponse

from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.shortcuts import render, redirect




class RegisterPageView(TemplateView):
    template_name = "Register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateUserForm()  # Make sure to import CreateUserForm
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user, user_profile = form.save()
            # You can access user and user_profile objects here
            return redirect('landing:index')  # Replace with your desired redirection

        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)
