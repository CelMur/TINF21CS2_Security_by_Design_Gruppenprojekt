# Generated by Django 4.2.7 on 2024-01-04 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement_point', '0006_alter_measurementpoint_household_size'),
        ('contract', '0010_remove_contract_measurement_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='measurement_point',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract', to='measurement_point.measurementpoint'),
        ),
    ]
