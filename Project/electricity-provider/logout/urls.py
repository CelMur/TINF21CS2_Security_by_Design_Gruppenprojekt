from django.urls import path
from .views import LogoutPageView
from django.contrib.auth.views import LogoutView
app_name = "logout"

urlpatterns = [
    path('', LogoutView.as_view(next_page='/'), name='logout'),
]
