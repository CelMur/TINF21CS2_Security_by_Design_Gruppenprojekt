from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        '''Create and save a user with the given email, and
        password.
        '''
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must have is_staff=True.'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have is_superuser=True.'
            )

        return self._create_user(email, password, **extra_fields)
class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    #username = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    email = models.EmailField(unique = True, max_length=255, blank=False) 
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager() 

    # Set unique related names for groups and user_permissions
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_user_permissions')

    class Meta:
        app_label = 'sign_up'
