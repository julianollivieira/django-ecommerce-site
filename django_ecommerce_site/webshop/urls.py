from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='webshop-home'),
    path('product/<int:product_id>', views.productdetails, name='webshop-productdetails'),
    path('login/', views.login, name='webshop-login'),
    path('register/', views.register, name='webshop-register')
]
