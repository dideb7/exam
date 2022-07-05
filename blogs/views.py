from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *


def index(request):
    posts = Article.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blogs/index.html', context=context)


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с {post_id}')


def show_category(request, cat_id):
    cats = Category.objects.all()
    posts = Article.objects.filter(pk=cat_id)
    context = {
        'cats': cats,
        'posts': posts,
        'cat_selected': cat_id
    }
    return render(request, 'women/index.html', context=context)