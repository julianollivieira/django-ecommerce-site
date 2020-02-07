from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import Product, User

# Classes for model specific methods
class Products:
    def getAll(self):
        return Product.objects.all()
    def getSearch(self, search_field, search_query):
        return Product.objects.raw('SELECT * FROM webshop_product WHERE '+search_field+' LIKE "%'+search_query+'%"')
    def getFields(self):
        return Product._meta.get_fields()
    def deleteWithId(self, _id):
        return Product.objects.filter(id=_id).delete()
    def getFirstWithId(self, _id):
        return Product.objects.filter(id=_id)[0]

class Users:
    def getAll(self):
        return User.objects.all()
    def getSearch(self, search_field, search_query):
        return User.objects.raw('SELECT * FROM webshop_user WHERE '+search_field+' LIKE "%'+search_query+'%"')
    def getFields(self  ):
        return User._meta.get_fields()
    def deleteWithId(self, _id):
        return User.objects.filter(id=_id).delete()
    def getFirstWithId(self, _id):
        return User.objects.filter(id=_id)[0]

categories = {
    'products': Products(),
    'users': Users(),
}

def overview(request, category):
    search_query = request.GET.get("query", "")
    search_field = request.GET.get("field", "") 
    cat = categories[category]

    items = cat.getAll() if search_query == "" else cat.getSearch(search_field, search_query)

    return render(request, 'webshop/panel/overview.html', {
        'category': category,
        'fields': cat.getFields(),
        'items': items,
        'search_query': search_query,
        'search_field': search_field,
    })

def delete(request, category, id):
    categories[category].deleteWithId(id)
    return redirect('/panel/'+category)

def edit(request, category, id):

    return render(request, 'webshop/panel/edit.html', {
        'category': category,
        'fields': categories[category].getFields(),
        'item': categories[category].getFirstWithId(id)
    })