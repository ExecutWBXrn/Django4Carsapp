from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Cars, Category
db_data = Cars.objects.all()

cat_db = Category.objects.all()

def index(request):
    context = {
        "title" : "lanos.com",
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

def cat(request):
    context={
        "title":"categories"
    }
    return render(request, 'carsmaincategory/category.html', context=context)

def dis_cat(request, cat_slug):
    w=get_object_or_404(Category, slug=cat_slug)
    context = {
        "title":w.name,
        "cat_slug":cat_slug,
        "db":db_data,
    }
    return render(request, "carsmaincategory/dis_cat.html", context=context)

def car_info(request, car_slug):
    w = get_object_or_404(Cars, slug=car_slug)
    context = {
        "title":w.title,
        "car_slug":car_slug,
        "db":db_data,
    }
    return render(request, "carsmaincategory/carinfo.html", context=context)

def Pagenotfound(request, exception):
    return HttpResponseNotFound("No hello world!")