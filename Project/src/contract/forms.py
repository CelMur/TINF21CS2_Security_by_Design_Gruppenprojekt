from django import forms
from .models import CustomerInfo

class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = ['meter_number', 'street', 'town', 'postal_number', 'terms_confirmed']
