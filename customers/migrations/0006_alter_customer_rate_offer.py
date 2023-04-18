# Generated by Django 3.2.10 on 2023-01-27 12:59

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_rename_offer_rate_customer_rate_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='rate_offer',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True),
        ),
    ]