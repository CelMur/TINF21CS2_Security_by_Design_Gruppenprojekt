import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.db import models
class UserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=45, unique=True)
    last_name = models.CharField(max_length=45, unique=True)
    email = models.EmailField(max_length=45,unique=True,blank=False)
    failed_login_attempts = models.IntegerField(default=0) #TODO: #is not yet beeing resetted
    last_login = models.DateTimeField(null=True, blank=True) 

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()