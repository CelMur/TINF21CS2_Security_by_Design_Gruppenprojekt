
from datetime import datetime
from typing import Any
from django.contrib.auth import get_user_model, authenticate
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.db import transaction

from .models import Contract

from measurement_point.views import CreateMeasurementPointView
from .serializers import ContractSerializerForCreate

from utils.logger import *
from utils.measurement_api import Api



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

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._logger = logging.getLogger(__name__)
        self.__api = Api.get_instance()


    def post(self, request, *args, **kwargs):
        user = self.request.user
        contract_id = request.data.get('id')
        password = request.data.get('confirmation_password')

        if not contract_id:
            return Response({"error": "Contract id is required."}, status=status.HTTP_400_BAD_REQUEST)

        if not password or not authenticate(username=user.get_username(), password=password):
            return Response({"error": "Password is required to cancel contract."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                contract = Contract.objects.get(id=contract_id, user=user)
                contract.is_active = False
                contract.end_date = datetime.now().date()
                contract.save()

                measurement_point = contract.measurement_point
                measurement_point.is_active = False
                measurement_point.save()

                self.__api.delete_meter(measurement_point.meter_uid)

                return Response({"success": "Contract cancelled."}, status=status.HTTP_200_OK)
                
        except Exception as e:
            self._logger.error(e, exc_info=True)
            return Response({"error": "Failed to cancel contract."}, status=status.HTTP_400_BAD_REQUEST)
    