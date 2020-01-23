from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'webshop/home.html')

def login(request):
    return render(request, 'webshop/login.html')

def register(request):
    return render(request, 'webshop/register.html')
