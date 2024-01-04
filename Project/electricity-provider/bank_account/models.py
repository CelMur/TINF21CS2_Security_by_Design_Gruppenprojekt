import uuid
from django.db import models
from django.conf import settings

# Create your models here.
class BankAccount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    iban = models.CharField(max_length=255)
    bic = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    has_sepa_mandate = models.BooleanField(default=False)

    class Meta:
        db_table = "bank_account"
        