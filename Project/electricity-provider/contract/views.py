
from datetime import datetime
from django.contrib.auth import get_user_model, authenticate
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from .models import Contract

from measurement_point.views import CreateMeasurementPointView
from .serializers import ContractSerializerForCreate

from utils.logger import *



# Create your views here.
class ContractView(ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ContractSerializerForCreate

    def get_queryset(self):
        user = self.request.user
        return Contract.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ContractViewCancel(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        contract_id = request.data.get('id')
        password = request.data.get('confirmation_password')

        if not contract_id:
            return Response({"error": "Contract id is required."}, status=status.HTTP_400_BAD_REQUEST)

        if not password or not authenticate(username=user.get_username(), password=password):
            return Response({"error": "Password is required to cancel contract."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            contract = Contract.objects.get(id=contract_id, user=user)
            contract.is_active = False
            contract.end_date = datetime.now().date()
            contract.save()

            return Response({"success": "Contract cancelled."}, status=status.HTTP_200_OK)
                
        except Exception as e:
            self._logger.error(e, exc_info=True)
            return Response({"error": "Failed to cancel contract."}, status=status.HTTP_400_BAD_REQUEST)
    