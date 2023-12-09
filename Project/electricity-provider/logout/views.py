from django.views.generic import TemplateView
from django.shortcuts import render, redirect

def LogoutPageView(request):
    if request.method == 'POST':
        return redirect('index.html')
        return render(request, 'index.html')