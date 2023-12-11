from django.urls import path
from .views import LogoutView

urlpatterns = [
    # Other url patterns...
    path('logout/', LogoutView.as_view(), name='logout'),
]