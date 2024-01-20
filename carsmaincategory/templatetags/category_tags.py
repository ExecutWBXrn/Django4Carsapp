from django import template
import carsmaincategory.views as views

register = template.Library()

@register.simple_tag(name="cat1")
def simpletag_cat():
    return views.cat_db

@register.simple_tag(name="menu")
def mainmenu():
    menu = [
        {"title": "head page", "url": "home"},
        {"title": "about site", "url": "about"},
        {"title": "favorites", "url": "fav"},
        {"title": "about us", "url": "info"},
        {"title": "log in", "url": "log"},
        {"title": "categories", "url":"cat"},
        {"title": "tags", "url":"tag_path"}
    ]
    return menu