from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def index(req):

    if req.method=="POST":
        name = req.POST.get("name")
        contact = req.POST.get("contact")

        Contact.objects.create(name=name, number=contact)
        

    return render (req, "index.html")