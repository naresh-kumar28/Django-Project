from django.shortcuts import render, redirect
from .models import Certificate

# Create your views here.

def header(req):
    return render(req, "header.html")

def certificate(req):

    data = Certificate.objects.all()

    return render(req, "certificate.html", {"certificates" : data})


def insert_form(req):

    if req.method=="POST":
        p = Certificate()
        p.certificate_id = req.POST.get("certificate_id")
        p.name = req.POST.get("name")
        p.age = req.POST.get("age")
        p.gender = req.POST.get("gender")
        p.id_verified = req.POST.get("id_verified")
        p.uhid = req.POST.get("uhid")
        p.reference_id = req.POST.get("reference_id")
        p.vaccination_status = req.POST.get("vaccination_status")
        p.vaccinated_by = req.POST.get("vaccinated_by")
        p.vaccinated_at = req.POST.get("vaccinated_at")
        p.dose_number = req.POST.get("dose_number")
        p.dose_date = req.POST.get("dose_date")
        p.vaccine_name = req.POST.get("vaccine_name")
        p.batch_number = req.POST.get("batch_number")
        p.vaccine_type = req.POST.get("vaccine_type")
        p.manufacturer = req.POST.get("manufacturer")

        p.save()

        return redirect(certificate)

    return render(req, "insert-data.html")