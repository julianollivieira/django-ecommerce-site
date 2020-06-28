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

def overview(request, category): # View items
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
def delete(request, category, id): # Delete items
    categories[category].deleteWithId(id)
    return redirect('/panel/'+category)
def edit(request, category, id): # Edit items
    if(request.GET.get("confirm", "") == "true"):

        record = categories[category].getFirstWithId(id)
        form_values = {}

        for field in categories[category].getFields():
            form_values[field.name] = request.POST.get("input-"+field.name, "")

        for key in form_values:
            setattr(record, key, form_values[key])

        record.save()
        return redirect("/panel/"+category)
    else:
        return render(request, 'webshop/panel/edit.html', {
            'category': category,
            'type': 'edit',
            'fields': categories[category].getFields(),
            'item': categories[category].getFirstWithId(id),
            'id': id,
        })
def add(request, category, id):
    if(request.GET.get("confirm", "") == "true"):
    

        return redirect("/panel/"+category)
    else:
        return render(request, 'webshop/panel/edit.html', {
            'category': category,
            'type': 'start',
            'fields': categories[category].getFields(),
            'item': categories[category].getFirstWithId(id),
            'id': id,
        })
