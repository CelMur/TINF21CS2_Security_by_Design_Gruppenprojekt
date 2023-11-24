from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm
from django.views import View

class SignUpPageView(View):
    template_name = "signup.html"

    def get(self, request):  # Change method name to 'get'
        form = SignupForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):  # Change method name to 'post'
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("USER SEND")
            login(request, user)
            return redirect("/pricing")  # Change 'home' to your desired redirect URL

        return render(request, self.template_name, {'form': form})
