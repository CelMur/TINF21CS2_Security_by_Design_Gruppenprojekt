from django.conf import settings
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ContractSerializer
from .models import Contract

# Create your views here.
class ContractView(ListCreateAPIView):

    if settings.DEBUG:
        authentication_classes = [TokenAuthentication]
    else:
        authentication_classes = [SessionAuthentication]

    permission_classes = [IsAuthenticated]
    serializer_class = ContractSerializer

    queryset = Contract.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Contract.objects.filter(user=user)
    #TODO: this function is complex and needs special attention, refactoring and probbably fixing :P
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)