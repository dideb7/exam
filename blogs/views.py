from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с {post_id}')