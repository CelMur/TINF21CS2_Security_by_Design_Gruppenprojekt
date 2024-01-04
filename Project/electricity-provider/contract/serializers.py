from datetime import datetime
from rest_framework import serializers
import django.db.transaction as transcaction

from energy_tariff.models import EnergyTariff
from address.models import Address
from bank_account.models import BankAccount
from measurement_point.models import MeasurementPoint
from .models import Contract

from address.serializers import AddressSerializer
from bank_account.serializers import BankAccountSerializer
from energy_tariff.serializers import EnergyTariffSerializer
from measurement_point.serializers import MeasurementPointSerializer
from utils.measurement_api import Api

from utils.logger import *


class ContractSerializerForCreate(serializers.ModelSerializer):
    address = AddressSerializer()
    billing_address = AddressSerializer()
    bank_account = BankAccountSerializer()

    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        self.__api = Api.get_Api()

    class Meta:
        model = Contract
        fields = [
            'id', 
            'start_date', 
            'end_date', 
            'user', 
            'address',
            'billing_address', 
            'bank_account', 
            'tariff', 
            'measurement_point'
        ]
        read_only_fields = [
            'id', 
            'user', 
            'start_date', 
            'end_date',
            'measurement_point'
        ]

    def create(self, validated_data):
        meter_uid = None
        try:
            with transcaction.atomic():
                address_data = validated_data.pop('address')
                billing_address_data = validated_data.pop('billing_address')
                bank_account_data = validated_data.pop('bank_account')
                tariff = validated_data.pop('tariff')

                user = self.context['request'].user

                meter_uid = self.__api.create_meter()
                
                addess, _ = Address.objects.get_or_create(user=user,**address_data)
                billing_address, _ = Address.objects.get_or_create(user=user,**billing_address_data)
                bank_account, _ = BankAccount.objects.get_or_create(user=user,**bank_account_data)

                measurement_point_serializer = MeasurementPointSerializer(data={'address':address_data},context=self.context)
                measurement_point_serializer.is_valid(raise_exception=True)
                measurement_point = measurement_point_serializer.save(meter_uid=meter_uid)


                # setting default values for contract
                start_date = datetime.now().date()
                end_date = None
                is_active = True
                price = tariff.price

                contract = Contract.objects.create(
                    address=addess,
                    billing_address=billing_address,
                    bank_account=bank_account,
                    measurement_point=measurement_point,
                    tariff=tariff,
                    price = price,
                    start_date=start_date,
                    end_date=end_date,
                    is_active=is_active,
                    **validated_data
                )

            return contract
        except Exception as e:
            logger.error(e, exc_info=True)
            if meter_uid:
                self.__api.delete_meter(meter_uid)
            raise e