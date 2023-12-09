from django import forms
from .models import Contract

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['street', 'city', 'postal_number', 'iban', 'terms_confirmed', 'debit_checked']
