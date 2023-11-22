from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class CreateUserForm():
    class Meta:
        model = User
        from django import forms
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib.auth.models import User

        class CreateUserForm(UserCreationForm):
            firstname = forms.CharField(max_length=30, required=True)
            lastname = forms.CharField(max_length=30, required=True)
            address = forms.CharField(max_length=255, required=True)
            city = forms.CharField(max_length=100, required=True)
            postal_code = forms.CharField(max_length=10, required=True)
            birth_date = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1900, 2023)))

            class Meta:
                model = User
                fields = ['firstname', 'lastname', 'address', 'city',
                          'postal_code', 'birth_date','email', 'password1', 'password2']