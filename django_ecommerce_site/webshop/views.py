from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'webshop/home.html')

def productdetails(request, product_id):
    return render(request, 'webshop/productdetails.html', {'product_id': product_id})

def login(request):
    return render(request, 'webshop/login.html')

def register(request):
    return render(request, 'webshop/register.html')
