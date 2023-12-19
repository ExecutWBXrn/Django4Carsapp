from django.urls import path, register_converter
from .views import *
from .convertors import superpuperconvertor

register_converter(superpuperconvertor, "duperpuper")

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('favorites/', fav, name="fav"),
    path('info/', info, name="info"),
    path('log/', log, name="log"),
    path('categories/', cat, name='cat'),
]