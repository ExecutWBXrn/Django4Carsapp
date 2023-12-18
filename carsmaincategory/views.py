from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

db_data = (
    {"id":1, "car":"lanos", "year":2007 ,"is_published":True},
    {"id":2, "car":"Tesla cybertruck", "year":2077 ,"is_published":False},
    {"id":3, "car":"ME", "year":"2005" ,"is_published":True},
)

def index(request):
    context = {
        "title" : "lanos.com",
        "mainmenu" : [
            {"title":"about site","url":"about"},
            {"title":"favorites","url":"fav"},
            {"title":"about us","url":"info"},
            {"title":"log in","url":"log"},
        ],
        "db_data":db_data,
    }
    return render(request, "carsmaincategory/index.html", context=context)

def about(request):
    context = {
        "title" : "lanos.com",
    }
    return render(request, "carsmaincategory/about.html", context=context)

def fav(request):
    return HttpResponse("page in developing")

def info(request):
    context={
        "title":"info",
    }
    return render(request, "carsmaincategory/finfo.html", context=context)

def log(request):
    return HttpResponse("this page in developing")

def Pagenotfound(request, exception):
    return HttpResponseNotFound("No hello world!")