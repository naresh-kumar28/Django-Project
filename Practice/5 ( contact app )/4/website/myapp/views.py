from django.shortcuts import render
from .models import Phonebook

# Create your views here.

def index(req):

    if req.method=="POST":
        name = req.POST.get("name")
        contact = req.POST.get("contact")

        Phonebook.objects.create(name=name, contact=contact)
        

    return render(req, 'index.html', {"person": Phonebook.objects.all()})