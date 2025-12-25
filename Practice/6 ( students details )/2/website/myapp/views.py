from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def callingPage(req):
    return render(req, 'callingData.html', {"details" : Student.objects.all()})

def insertData(req):

    if req.method=="POST":
        name = req.POST.get("name")
        contact = req.POST.get("contact")
        email = req.POST.get("email")
        father_name = req.POST.get("father_name")
        school_name = req.POST.get("school_name")
        maths = req.POST.get("maths")
        science = req.POST.get("science")
        sst = req.POST.get("sst")
        hindi = req.POST.get("hindi")
        english = req.POST.get("english")

        #save data in database
        Student.objects.create(
            name = name,
            contact = contact,
            email = email,
            fathername = father_name,
            schoolname = school_name,
            math = maths,
            sci = science,
            sst = sst,
            hindi = hindi,
            eng = english,
        )
        return redirect(insertData)
        
    return render(req, 'insertData.html')