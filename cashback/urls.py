from django.urls import path
from . import views

urlpatterns = [
    path('cashback/', views.CashbackList.as_view()),
    path('customer/', views.CustomerList.as_view()),
    path('product/', views.ProductList.as_view())
]
