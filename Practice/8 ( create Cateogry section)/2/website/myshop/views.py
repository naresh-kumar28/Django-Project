from django.shortcuts import render, redirect
from .models import Category, Product

# Create your views here.

def homepage(req):

    data = {}
    data['categories'] = Category.objects.all()
    data['products'] = Product.objects.all()
    return render(req, "home.html", data)



def insertpage(req):

    if req.method =="POST":
        p = Product()
        p.name = req.POST.get("name")
        p.price = req.POST.get("price")
        p.description = req.POST.get("description")
        p.discount_price = req.POST.get("discount_price")
        p.image = req.FILES.get("image")
        
        
        cat_id = req.POST.get("category")
        p.Category = Category.objects.get(id = cat_id)
        p.save()

        return redirect(homepage)
        
    return render(req, "insert-data.html", {"categories" : Category.objects.all()})