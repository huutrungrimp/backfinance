# Generated by Django 3.2.10 on 2023-01-29 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_auto_20230129_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_time_end',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 29, 13, 47, 0, 925836)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_time_start',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 29, 13, 47, 0, 925836)),
        ),
    ]
