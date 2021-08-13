from .models import Cashback, Customer, Product
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CashbackSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(required=False, read_only=True)
    product = ProductSerializer(required=False, read_only=True)

    class Meta:
        model = Cashback
        fields = '__all__'
