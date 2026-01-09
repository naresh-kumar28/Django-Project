from django.shortcuts import render, redirect
from.models import Products

# Create your views here.

def home(req):
    data = Products.objects.all()

    return render(req, 'home.html', {"products" : data})


def insert_data(req):

    if req.method=="POST":
        p = Products()
        p.name = req.POST.get('name')
        p.price = req.POST.get('price')
        p.description = req.POST.get('description')
        p.image = req.FILES.get('image')

        p.save()

        return redirect('/')


    return render(req, 'insert-data.html')