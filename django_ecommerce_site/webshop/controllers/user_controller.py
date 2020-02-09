from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import Product, User

def login(request):
    return render(request, 'webshop/user/login.html')

def signup(request):
    return render(request, 'webshop/user/signup.html')


# Logout and account PAGE
def account(request):
    return render(request, 'webshop/login.html', {'error': request.GET.get('error')})

def logout(request):
    return render(request, 'webshop/register.html', {'error': request.GET.get('error')})



# Login and register API ROUTES
def api_login(request):
    user = User.objects.filter(email = request.POST.get("email", ""))

    if(user):
        if(user[0].password == request.POST.get("password", "")):
            return redirect('/')
        else:
            error = "Wrong password!"
    else:
        error = "User does not exist!"
    
    return redirect('/login/?error=' + error)
    

def api_register(request):

    error = 'A user with email already exists.'

    if False:
        return redirect('/')
    else:
        return redirect('/register/?error=' + error)
    