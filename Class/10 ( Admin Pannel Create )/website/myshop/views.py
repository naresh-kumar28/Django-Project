from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(req):
    data = {}

    if 'cat_id' in req.GET:
        cat_id = req.GET.get('cat_id')
        data["products"] = Product.objects.filter(category=cat_id)

    elif 'search' in req.GET:
        search = req.GET.get("search")
        data["products"] = Product.objects.filter(name__icontains=search)

    else:
        data['products'] = Product.objects.all()

    data['categories'] = Category.objects.all()
    return render(req, "home.html", data)


def addCategory(req):
    if req.method=="POST":
        c = Category()
        c.title = req.POST.get("add_cat")
        c.save()

        return redirect(addCategory)
    return render(req, "add-category.html", {"categories" : Category.objects.all()})


def insertpage(req):

    if req.method=="POST":
        p = Product()
        p.name = req.POST.get("name")
        p.price = req.POST.get("price")
        p.discount_price = req.POST.get("discount_price")
        p.description = req.POST.get("description")
        p.image = req.FILES.get("image")

        cat_id = req.POST.get("category")
        p.category = Category.objects.get(id=cat_id)

        p.save()

        return redirect(home)

    return render(req, "insert-data.html", {"categories" : Category.objects.all()})


def viewDetails(req, product_id):
    data={}
    data['product'] = Product.objects.get(id=product_id)
    data['categories'] = Category.objects.all()
    return render(req, "view-details.html", data)