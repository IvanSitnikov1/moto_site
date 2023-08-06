from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *


menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):
    posts = Motorcycle.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'menu': menu, 'posts': posts})


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')