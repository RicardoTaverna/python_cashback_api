from django.contrib import admin
from .models import Cashback, Customer, Product

# Register your models here.

admin.site.register(Cashback)
admin.site.register(Customer)
admin.site.register(Product)
