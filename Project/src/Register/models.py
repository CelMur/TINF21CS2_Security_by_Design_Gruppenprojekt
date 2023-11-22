from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)

    def __str__(self):
        return self.text

    class Meta:
        app_label = 'Register'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username

    class Meta:
        app_label = 'Register'
