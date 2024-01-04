from rest_framework.response import Response
from rest_framework import status
from .models import BankAccount
from .serializers import CreateBankAccountSerializer, ReadBankAccountSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView

class BankAccountView(ListCreateAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = CreateBankAccountSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadBankAccountSerializer
        return CreateBankAccountSerializer

    def get_queryset(self):
        user = self.request.user
        bank_accounts = BankAccount.objects.filter(user=user)
        return bank_accounts

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
