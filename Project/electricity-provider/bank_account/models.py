from django.db import models
from django.conf import settings

# Create your models here.
class BankAccount(models.Model):
    #TODO: chage id from deterministic int to random uuid4 => db migration required
    #TODO:Provide default values for all fields except iban and user
    iban = models.CharField(max_length=255, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    has_sepa_mandate = models.BooleanField(default=False)

    class Meta:
        db_table = "bank_account"