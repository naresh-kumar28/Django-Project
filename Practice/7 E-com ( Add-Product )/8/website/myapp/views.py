from django.shortcuts import render, redirect
from .models import Product

# Create your views here.

def home(req):
    data = Product.objects.all()

    return render(req, "home.html", {"items" : data})


def insert_page(req):

    if req.method=="POST":
        p = Product()
        p.price = req.POST.get("price")
        p.name = req.POST.get("name")
        p.description = req.POST.get("description")
        p.image = req.FILES.get("image")

        p.save()

        return redirect(home)

    return render(req, "insert-data.html")