# Generated by Django 4.2.7 on 2023-12-10 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0005_contract_household_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='household_size',
        ),
    ]
