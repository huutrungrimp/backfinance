from rest_framework import serializers
from .models import Customer
from accounts.serializers import UserSerializer


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'user', 'customerName', 'email', 'phone', 'address', 'city', 'province', 'postal', 'province', 'country', 'rate_offer']