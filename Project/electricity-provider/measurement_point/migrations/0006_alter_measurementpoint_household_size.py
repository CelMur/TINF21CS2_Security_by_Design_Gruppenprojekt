# Generated by Django 4.2.7 on 2024-01-04 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement_point', '0005_remove_measurementpoint_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurementpoint',
            name='household_size',
            field=models.IntegerField(default=0),
        ),
    ]
