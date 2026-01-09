from django.shortcuts import render, redirect
from .models import StudentRecord

# Create your views here.

def home_page(req):
    return render(req, "calling-data.html", {"details" : StudentRecord.objects.all()})

def inset_data(req):

    if req.method=="POST":
        name = req.POST.get("name")
        contact = req.POST.get("contact")
        email = req.POST.get("email")
        school = req.POST.get("school_name")
        father = req.POST.get("father_name")
        math = req.POST.get("maths")
        hindi = req.POST.get("hindi")
        science = req.POST.get("science")
        sst = req.POST.get("sst")
        english = req.POST.get("english")

        #Save data in models ( create class object )
        std = StudentRecord()
        std.name = name
        std.contact = contact
        std.email = email
        std.school_name = school
        std.father_name = father
        std.math = math
        std.hindi = hindi
        std.science = science
        std.sst = sst
        std.english = english
        std.save()

        return redirect(home_page)

    return render(req, "insert-data.html")