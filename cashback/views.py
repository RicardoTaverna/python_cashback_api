from rest_framework import generics

from .models import Cashback, Customer, Product
from .serializers import CashbackSerializer, CustomerSerializer, ProductSerializer

# Create your views here.


class CashbackList(generics.ListCreateAPIView):
    queryset = Cashback.objects.all()
    serializer_class = CashbackSerializer


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
