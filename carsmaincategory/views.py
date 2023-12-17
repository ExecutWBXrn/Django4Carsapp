from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

db_data = (
    {"id":1, "car":"lanos", "year":2007 ,"is_published":True},
    {"id":2, "car":"Tesla cybertruck", "year":2077 ,"is_published":True},
    {"id":3, "car":"ME", "year":"2005" ,"is_published":True},
)

def index(request):
    context = {
        "title" : "lanos.com",
        "mainmenu" : ["about site", "favorites", "about us", "log in"],
        "db_data":db_data,
    }
    return render(request, "carsmaincategory/index.html", context=context)

def about(request):
    context = {
        "title" : "lanos.com",
    }
    return render(request, "carsmaincategory/about.html", context=context)

def Pagenotfound(request, exception):
    return HttpResponseNotFound("No hello world!")