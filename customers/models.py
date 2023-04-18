from django.db import models
from accounts.models import User
from decimal import Decimal

# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    customerName = models.CharField(null=True, blank=True, max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True, max_length=15)
    address = models.CharField(null=True, blank=True, max_length=255)
    city = models.CharField(null=True, blank=True, max_length=255)
    province = models.CharField(null=True, blank=True, max_length=255)
    postal = models.CharField(null=True, blank=True, max_length=255)
    country = models.CharField(null=True, blank=True, max_length=255)
    rate_offer = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=Decimal('0.00'))  

    def __str__(self):
        return str(self.customerName)
