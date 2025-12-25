from django.shortcuts import render, redirect
from .models import phonebook

# Create your views here.

def index(req):

    if req.method=="POST":
        name = req.POST.get("name")
        contact = req.POST.get("contact")

        contact_list = phonebook.objects.create(name=name, number=contact)
        return redirect(index)

    return render(req, "index.html", {"person" : phonebook.objects.all()})