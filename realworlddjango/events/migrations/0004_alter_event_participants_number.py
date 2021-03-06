# Generated by Django 4.0.1 on 2022-05-29 07:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_participants_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='participants_number',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Количество участников'),
        ),
    ]
