from django.shortcuts import HttpResponse

def home(req):
    return HttpResponse("<h1>Hello World</h1>")