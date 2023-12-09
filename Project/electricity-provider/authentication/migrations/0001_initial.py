# Generated by Django 4.2.7 on 2023-12-09 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=45, unique=True)),
                ('last_name', models.CharField(max_length=45, unique=True)),
                ('email', models.EmailField(max_length=45, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
