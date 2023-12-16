from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return render(request, "carsmaincategory/index.html")

def about(request):
    return render(request, "carsmaincategory/about.html")

def Pagenotfound(request, exception):
    return HttpResponseNotFound("No hello world!")