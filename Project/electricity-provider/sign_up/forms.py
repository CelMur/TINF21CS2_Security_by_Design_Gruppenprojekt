from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    #email = forms.EmailField(max_length=200, help_text='Required')
    pass
    class Meta:
        model = CustomUser
        fields = ['id','firstname', 'lastname', 'address', 'city', 'postal_code', 'email', 'password1', 'password2']
