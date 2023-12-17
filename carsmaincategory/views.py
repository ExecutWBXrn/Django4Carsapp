from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    context = {
        "title" : "lanos.com",
    }
    return render(request, "carsmaincategory/index.html", context=context)

def about(request):
    context = {
        "title" : "lanos.com",
    }
    return render(request, "carsmaincategory/about.html", context=context)

def Pagenotfound(request, exception):
    return HttpResponseNotFound("No hello world!")