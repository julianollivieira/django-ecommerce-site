from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import Product, User

# Home
def home(request):
    return render(request, 'webshop/home.html', {'products': Product.objects.all()})

# Product details
def product(request, product_id):
    return render(request, 'webshop/productdetails.html', {'product_id': product_id})

# Shopping cart overview
def shopping_cart(request):
    return render(request, 'webshop/shopping_cart.html')
