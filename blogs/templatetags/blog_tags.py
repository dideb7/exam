from django import template
from blogs.models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]

register = template.Library()


@register.inclusion_tag('blogs/list_menu.html')
def get_menu():
    return {'menu': menu}


@register.inclusion_tag('blogs/list_cat.html')
def get_cat(cat_select=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_select}