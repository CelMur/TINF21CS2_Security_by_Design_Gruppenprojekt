from django.core.management.base import BaseCommand
from ...models import EnergyTariff  # replace 'myapp' with your actual app name

class Command(BaseCommand):
    help = 'Create initial data for EnergyTariff'

    def handle(self, *args, **kwargs):
        EnergyTariff.objects.get_or_create(name='Standard Plan', defaults={'price': 30.00, 'renewable': 0.3})
        EnergyTariff.objects.get_or_create(name='Premium Plan', defaults={'price': 31.00, 'renewable': 0.5})
        EnergyTariff.objects.get_or_create(name='Green Plan', defaults={'price': 28.00, 'renewable': 1.0})

        self.stdout.write(self.style.SUCCESS('Successfully created 3 EnergyTariff entries'))