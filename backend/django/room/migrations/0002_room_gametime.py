# Generated by Django 5.1.1 on 2024-12-23 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='gametime',
            field=models.FloatField(default=30),
        ),
    ]
