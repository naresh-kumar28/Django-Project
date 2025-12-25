from django.shortcuts import HttpResponse

def home(req):
    return HttpResponse("<h1>Hello world</h1>")