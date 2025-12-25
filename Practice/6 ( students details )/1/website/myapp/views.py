from django.shortcuts import render, redirect
from .models import Student
# Create your views here.

def callingPage(req):
    return render(req,'callingData.html', {"data" : Student.objects.all()})

def insertPage(req):

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

        std = Student()
        std.name = name
        std.contact = contact
        std.email = email
        std.fathername = father_name
        std.schoolname = school_name
        std.math = maths
        std.sci = science
        std.sst = sst
        std.hin = hindi
        std.eng = english
        std.save()

        return redirect(insertPage)
    
    return render(req,'insertData.html')