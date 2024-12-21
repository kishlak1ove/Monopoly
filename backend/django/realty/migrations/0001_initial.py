# Generated by Django 5.1.1 on 2024-12-21 20:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0001_initial'),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.IntegerField()),
                ('position', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.player')),
            ],
        ),
    ]
