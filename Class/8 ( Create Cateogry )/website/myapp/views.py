from django.shortcuts import render, redirect
from .models import Category, Product

# Create your views here.

def home(req):
    data = {}

    if 'cat_id' in req.GET:
        cat_id = req.GET.get('cat_id')
        data['products'] = Product.objects.filter(category=cat_id)

    elif 'search' in req.GET:
        search = req.GET.get("search")
        data['products'] = Product.objects.filter(name__icontains=search)

    else:
        data["products"] = Product.objects.all()

    data["categories"] = Category.objects.all()
    return render(req, "home.html", data)

def productview(req, product_id):
    data = {}
    data['product'] = Product.objects.get(id=product_id)
    return render(req, "product-view.html", data)