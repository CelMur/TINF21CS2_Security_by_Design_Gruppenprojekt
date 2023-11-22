from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile  # Import the UserProfile model

class CreateUserForm(UserCreationForm):
    # Your additional fields
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    postal_code = forms.CharField(max_length=10)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'firstname', 'lastname', 'address', 'city', 'postal_code']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']
        user.email = self.cleaned_data['email']
        user.save()

        # Custom fields
        user_profile = UserProfile.objects.create(
            user=user,
            address=self.cleaned_data['address'],
            city=self.cleaned_data['city'],
            postal_code=self.cleaned_data['postal_code'],
        )

        return user, user_profile
