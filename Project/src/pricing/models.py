from django.db import models
from django.contrib.sites.models import Site

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=140,blank=False, null=False)

    def __str__(self):
        return self.text

    @classmethod
    def add_additional_sites(cls):
        # Create additional Site instances
        green_plan = Site.objects.create(name='Green Plan')
        premium_plan  = Site.objects.create( name='Premium Plan')
        standard_plan = Site.objects.create(name='Standard Plan')