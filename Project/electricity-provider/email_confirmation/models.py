
from django.utils import timezone
from datetime import timedelta
from django.conf import settings

from django.db import models

def seven_days_from_now():
    return timezone.now() + timedelta(days=7)

class EmailConfirmation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=45)
    second_token = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    action = models.CharField(max_length=45)
    context = models.TextField()
    expiration_data = models.DateTimeField(default=seven_days_from_now)
    claimed = models.BooleanField(default=False)
    claimed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "email_confirmation"


    def has_expired(self):
        return timezone.now() > self.expiration_data