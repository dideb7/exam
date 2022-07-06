from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import *
from .forms import AddPF


def index(request):
    posts = Article.objects.all()
    context = {
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'blogs/index.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Article, slug=post_slug)
    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'blogs/post.html', context=context)


def show_category(request, cat_slug):
    marker = get_object_or_404(Category, slug=cat_slug)
    cat_id = marker.pk
    posts = Article.objects.filter(cat_id=cat_id)
    context = {
        'posts': posts,
        'cat_selected': cat_id,
    }
    return render(request, 'blogs/index.html', context=context)


def addpage(request):
    if request.method == 'POST':
        form = AddPF(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPF()
    return render(request, 'blogs/addpage.html', {'form': form, 'title': 'Добавление статьи'})
