from django.shortcuts import render, redirect
from .models import Phonebook

# Create your views here.

def home(req):

    if req.method=="POST":
        name = req.POST.get("name")
        contact = req.POST.get("contact")
        
        info = Phonebook.objects.create(name=name, number=contact) #save data in models variable
        return redirect(home)
        
    return render(req, "home.html", {"contacts" : Phonebook.objects.all()}) #show data in html page