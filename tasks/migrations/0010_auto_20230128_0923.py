# Generated by Django 3.2.10 on 2023-01-28 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_auto_20230128_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_time_end',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 28, 9, 23, 3, 443767)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_time_start',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 28, 9, 23, 3, 443767)),
        ),
    ]
