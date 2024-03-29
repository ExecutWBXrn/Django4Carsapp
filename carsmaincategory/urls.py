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
    path('categories/<slug:cat_slug>', dis_cat, name='dcat'),
    path('car/<slug:car_slug>', car_info, name="carinfo"),
    path('tag/', tag, name="tag_path"),
    path('tag/<slug:tag_slug>', tag_tag_slug, name="tag_slug_path"),
]