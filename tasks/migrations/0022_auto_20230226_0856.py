# Generated by Django 3.2.10 on 2023-02-26 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0021_auto_20230226_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_time_end',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 26, 8, 56, 6, 183815)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_time_start',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 26, 8, 56, 6, 183815)),
        ),
    ]
