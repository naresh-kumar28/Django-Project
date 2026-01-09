from django.shortcuts import render, redirect
from .models import Certificate

# Create your views here.

def header(req):
    return render(req, "header.html")

def viewlist(req):
    return render(req, "view-list.html")

def certificate(req):

    data = Certificate.objects.all()

    return render(req, "certificate.html", {"certificates" : data})


def insert_form(req):

    if req.method == "POST":
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

        # dose 1 (mandatory)
        p.dose_number1 = req.POST.get("dose_number1")
        p.dose_date1 = req.POST.get("dose_date1")
        p.vaccine_name1 = req.POST.get("vaccine_name1")
        p.batch_number1 = req.POST.get("batch_number1")
        p.vaccine_type1 = req.POST.get("vaccine_type1")
        p.manufacturer1 = req.POST.get("manufacturer1")

        # dose 2 (optional)
        p.dose_number2 = req.POST.get("dose_number2")
        dose_date2 = req.POST.get("dose_date2")
        p.dose_date2 = dose_date2 if dose_date2 else None
        p.vaccine_name2 = req.POST.get("vaccine_name2")
        p.batch_number2 = req.POST.get("batch_number2")
        p.vaccine_type2 = req.POST.get("vaccine_type2")
        p.manufacturer2 = req.POST.get("manufacturer2")

        # dose 3 (optional)
        p.dose_number3 = req.POST.get("dose_number3")
        dose_date3 = req.POST.get("dose_date3")
        p.dose_date3 = dose_date3 if dose_date3 else None
        p.vaccine_name3 = req.POST.get("vaccine_name3")
        p.batch_number3 = req.POST.get("batch_number3")
        p.vaccine_type3 = req.POST.get("vaccine_type3")
        p.manufacturer3 = req.POST.get("manufacturer3")

        p.save()
        return redirect(certificate)

    return render(req, "insert-data.html")
