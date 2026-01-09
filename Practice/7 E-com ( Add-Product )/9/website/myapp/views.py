from django.shortcuts import render, redirect
from .models import Product

# Create your views here.

def home(req):

    #Show data in HTML Page
    data = Product.objects.all()
    return render(req, "home.html", {"products" : data})


def insert_page(req):

    #Save data in models variables
    if req.method=="POST":
        p = Product()
        p.name = req.POST.get("name")
        p.price = req.POST.get("price")
        p.description = req.POST.get("description")
        p.image = req.FILES.get("image")
        p.save()

        return redirect(home)
        
    return render(req, "insert-data.html")