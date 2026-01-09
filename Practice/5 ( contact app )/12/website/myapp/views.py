from django.shortcuts import render,redirect
from .models import Contact

# Create your views here.

def home(req):

    if req.method=="POST":
        name = req.POST.get("name")
        contact = req.POST.get("contact")

        Contact.objects.create(name=name, contact=contact)
        return redirect(home)

    return render(req,"index.html", {"person" : Contact.objects.all()})