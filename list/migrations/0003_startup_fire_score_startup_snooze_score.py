# Generated by Django 4.2.7 on 2023-11-15 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_startup_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='fire_score',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='startup',
            name='snooze_score',
            field=models.BigIntegerField(default=0),
        ),
    ]
