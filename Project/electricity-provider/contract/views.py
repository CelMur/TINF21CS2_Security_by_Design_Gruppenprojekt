
from django.conf import settings
from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from address.models import Address
from measurement_point.views import CreateMeasurementPointView
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
        address_data = self.request.data.get('address')
        billing_address_data = self.request.data.get('billing_address')

        #if any step fails, the whole process must fail!

        if isinstance(address_data, int):  # address reference provided
            address = Address.objects.get(id=address_data)
        else:  # address data provided
            address = Address.objects.create(**address_data)

        if isinstance(billing_address_data, int):
            billing_address = Address.objects.get(id=billing_address_data)
        else:
            billing_address = Address.objects.create(**billing_address_data)

            #TODO: create measurement point!!!!!!!!!!!!!!
            measurement_point = None

        serializer.save(user=self.request.user, address=address, billing_address=billing_address, measurement_point=measurement_point)