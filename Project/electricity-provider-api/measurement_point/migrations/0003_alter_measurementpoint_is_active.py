# Generated by Django 4.2.7 on 2023-12-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement_point', '0002_remove_measurementpoint_contract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurementpoint',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
