from django.shortcuts import render,redirect
from .models import Phonebook

# Create your views here.

def index(request):

    if request.method=="POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")

        contactlist = Phonebook.objects.create(name=name, contact=contact)
        return redirect(index)
        
        
    return render(request,'index.html', {"details" : Phonebook.objects.all()})

