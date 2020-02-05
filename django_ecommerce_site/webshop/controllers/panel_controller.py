from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import Product, User

# Panel
def main(request):
    return render(request, 'webshop/panel/panel.html')


# Overview
def users(request):
    query = request.GET.get("query", "")
    field = request.GET.get("field", "")

    if(query == ""):
        users = User.objects.all()
    else:
        if(field == "email"):
            users = User.objects.filter(email__contains = query)
        elif(field == "gender"):
            users = User.objects.filter(gender__contains = query)
        elif(field == "first name"):
            users = User.objects.filter(first_name__contains = query)
        elif(field == "last name"):
            users = User.objects.filter(last_name__contains = query)
        else:
            users = User.objects.all()

    return render(request, 'webshop/panel/user_overview.html', {
        'users': users, 
        'query': query, 
        'fields': [
            {'field': 'Email', 'value': True if field == "email" else False},
            {'field': 'Gender', 'value': True if field == "gender" else False},
            {'field': 'First Name', 'value': True if field == "first name" else False},
            {'field': 'Last Name', 'value': True if field == "last name" else False}
        ]
    })

def products(request):
    query = request.GET.get("query", "")
    field = request.GET.get("field", "")

    if(query == ""):
        products = Product.objects.all()
    else:
        if(field == "title"):
            products = Product.objects.filter(title__contains = query)
        elif(field == "description"):
            products = Product.objects.filter(description__contains = query)
        else:
            products = Product.objects.all()

    return render(request, 'webshop/panel/product_overview.html', {
        'products': products, 
        'query': query, 
        'fields': [
            {'field': 'Title', 'value': True if field == "title" else False},
            {'field': 'Description', 'value': True if field == "description" else False}
        ]
    })

# Delete
def delete_user(request):
    # Delete users here
    message = "User deleted succesfully!"
    return redirect('/panel/users/?message=' + message) # Add color? info/warning/danger

def delete_product(request):
    # Delete users here
    message = "Product deleted succesfully!"
    return redirect('/panel/products/?message=' + message) # Add color? info/warning/danger

# Add
def add_user(request):
    # Add users here
    message = "User added succesfully!"
    return redirect('/panel/users/?message=' + message) # Add color? info/warning/danger

def add_product(request):
    # Add products here
    message = "Product added succesfully!"
    return redirect('/panel/products/?message=' + message) # Add color? info/warning/danger

# Add
def edit_user(request):
    # Edit users here
    message = "User edited succesfully!"
    return redirect('/panel/users/?message=' + message) # Add color? info/warning/danger

def edit_product(request):
    # Edit products here
    message = "Product edited succesfully!"
    return redirect('/panel/products/?message=' + message) # Add color? info/warning/danger
