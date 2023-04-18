# Generated by Django 3.2.10 on 2023-01-17 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('province', models.CharField(blank=True, max_length=255, null=True)),
                ('postal', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]
