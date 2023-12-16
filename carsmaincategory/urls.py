from django.urls import path, register_converter
from .views import *
from .convertors import superpuperconvertor

register_converter(superpuperconvertor, "duperpuper")

urlpatterns = [
    path('', index),
]