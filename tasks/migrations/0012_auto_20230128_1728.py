# Generated by Django 3.2.10 on 2023-01-28 22:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_auto_20230128_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_time_end',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 28, 17, 28, 36, 600383)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_time_start',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 28, 17, 28, 36, 600383)),
        ),
    ]