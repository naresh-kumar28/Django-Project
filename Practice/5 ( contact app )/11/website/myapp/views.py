from django.shortcuts import render
from .models import phonebook

# Create your views here.

def index(req):

    if req.method=="POST":
        name = req.POST.get("name")
        contact = req.POST.get("contact")

        phonebook.objects.create(name=name, number=contact)

    return render(req, 'index.html', {"person" : phonebook.objects.all()})