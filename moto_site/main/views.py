from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *


menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

def index(request):
    posts = Motorcycle.objects.all()
    context = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    return render(request, 'main/about.html', {'title': 'О сайте', 'menu': menu})


def addpage(request):
    return HttpResponse('Дбавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')