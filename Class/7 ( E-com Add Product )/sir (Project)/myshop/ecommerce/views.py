from django.shortcuts import render, redirect
from .models import Product

# Create your views here.

def home(req):
    data = Product.objects.all()
    return render(req, "home.html", {"products" : data})

def insert_product(req):

    if req.method=="POST":
        p = Product()
        p.name = req.POST.get("name")
        p.price = req.POST.get("price")
        p.description = req.POST.get("description")
        p.image = req.FILES.get("image")
        p.save()

        return redirect('/')
        
    return render(req, "insert_product.html")