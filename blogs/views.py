from pprint import pprint

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import AddPF
from django.views.generic import ListView, DeleteView, CreateView
from .utils import *


class ArticlHome(DataMixin, ListView):
    model = Article
    template_name = 'blogs/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная старница')
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DataMixin, DeleteView):
    model = Article
    template_name = 'blogs/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class ArticleCategory(DataMixin, ListView):
    model = Article
    template_name = 'blogs/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Article.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPF
    template_name = 'blogs/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление поста')
        return dict(list(context.items()) + list(c_def.items()))