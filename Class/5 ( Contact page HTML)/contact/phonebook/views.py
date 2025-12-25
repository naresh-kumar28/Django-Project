from django.shortcuts import render, redirect
from phonebook.models import Vcard

# Create your views here.

def index(req):

    if req.method=="POST":
        name = req.POST.get("name")
        contact = req.POST.get("contact")

        newvcard = Vcard.objects.create(name=name, phone_no = contact)

        return redirect (index)

    return render (req, "index.html" , {"vcarditems" : Vcard.objects.all()})