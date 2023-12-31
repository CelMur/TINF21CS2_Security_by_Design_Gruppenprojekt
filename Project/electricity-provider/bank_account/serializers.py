
import uuid
from rest_framework import serializers
from .models import BankAccount

from utils.logger import *

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('id', 'iban', 'user', 'bic', 'name')
        read_only_fields = ('id','user')
        
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data.pop('user', None)
        bank_account, created = BankAccount.objects.get_or_create(user=user, **validated_data)
        return bank_account

class ReadBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        exclude = ('user','has_sepa_mandate','balance')
