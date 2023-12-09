from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

class LogoutPageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse(''))  # 'home' ist der Name der Ansicht, zu der Sie nach dem Logout umleiten möchten