from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("Hello world!")

def Pagenotfound(request, exception):
    return HttpResponseNotFound("No hello world!")