# Generated by Django 4.2.7 on 2024-01-04 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0009_alter_contract_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='measurement_point',
        ),
    ]
