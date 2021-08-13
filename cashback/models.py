from django.db import models

# Create your models here.


class Customer(models.Model):
    """Modelo para os dados do cliente.

    Args:
        models ([type]): [description]
    """
    document = models.CharField(max_length=11)
    name = models.CharField(max_length=120)


class Product(models.Model):
    """Modelo para os dados do produto.

    Args:
        models ([type]): [description]
    """
    KIND_CHOICES = [
        ('A', 'tipo A'),
        ('B', 'tipo B'),
        ('C', 'tipo C')
    ]

    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    value = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)


class Cashback(models.Model):
    """Modelo para os dados do cashback.

    Args:
        models ([type]): [description]
    """
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    sold_at = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(null=True, blank=True)
