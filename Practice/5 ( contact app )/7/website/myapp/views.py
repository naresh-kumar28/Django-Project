from django.shortcuts import render,redirect
from .models import Phonebook

# Create your views here.

def index(req):

    if req.method=="POST":
        name = req.POST.get("name")
        contact = req.POST.get("contact")

        newcard = Phonebook.objects.create(name=name, number=contact)
        return redirect (index) 

    return render(req,"index.html", {"person" : Phonebook.objects.all()})
