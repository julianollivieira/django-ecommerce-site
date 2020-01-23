from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='webshop-home'),
    path('login/', views.login, name='webshop-login'),
    path('register/', views.register, name='webshop-register')
]
