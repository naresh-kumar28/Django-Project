from django.shortcuts import render
from .models import Phonebook

# Create your views here.

def index(req):

    if req.method=="POST":
        name = req.POST.get("name")
        contact = req.POST.get("contact")

        Phonebook.objects.create(name=name, number=contact)

    return render(req, 'index.html')