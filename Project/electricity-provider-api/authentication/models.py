import uuid
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=45, unique=True)
    last_name = models.CharField(max_length=45, unique=True)
    email = models.EmailField(max_length=45,unique=True,blank=False)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
