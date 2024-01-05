
from django.utils import timezone
from datetime import timedelta
from django.conf import settings

from django.db import models


class EmailFailedLogins(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "email_failed_logins"


