from django import template
from blogs.models import *

register = template.Library()


@register.inclusion_tag('blogs/list_cat.html')
def get_cat(cat_select=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_select}
