# Generated by Django 3.2.10 on 2023-04-18 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0025_auto_20230418_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_time_end',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 18, 9, 33, 46, 36569)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_time_start',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 18, 9, 33, 46, 36569)),
        ),
    ]
