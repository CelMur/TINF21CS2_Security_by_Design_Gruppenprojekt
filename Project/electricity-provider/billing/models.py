# contract_viewer/models.py
from sign_up.models import CustomUser
from user_dashboard.models import Contract
from django.db import models


class Bills(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    month = models.DateField()
    kwh = models.FloatField()
    billing_amount = models.FloatField()
    billing_status = models.CharField(max_length=50)

    @property
    def object_name(self):
        return f"{self.contract.address}, {self.contract.postal_code}, {self.contract.city}"
