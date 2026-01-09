from django.shortcuts import render
from .models import Product, Category


def dashboard(req):
    return render(req, "admin/dashboard.html")


def manageProduct(req):
    data = {}
    data['products'] = Product.objects.all()
    return render(req, "admin/manageProduct.html", data)


def manageCategory(req):
    data = {}
    data['categories'] = Category.objects.all()
    return render(req, "admin/manageCategory.html", data)