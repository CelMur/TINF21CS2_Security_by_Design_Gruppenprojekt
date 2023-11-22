
from django.forms import inlineformset_factory
from django.http import HttpResponse

from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from Register.forms import CreateUserForm
from django.shortcuts import render, redirect




class RegisterPageView(TemplateView):
    template_name = "Register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateUserForm()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # Save the user and perform any additional actions
            form.save()
            # Redirect to a success page or any other appropriate action
            return redirect('landing:index')  #TODO Replace 'landing:index' with the actual URL you want to redirect to

        # If the form is not valid, re-render the page with the form and errors
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)