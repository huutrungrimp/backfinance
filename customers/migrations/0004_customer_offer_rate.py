# Generated by Django 3.2.10 on 2023-01-27 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20230125_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='offer_rate',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]