from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import *


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
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'main/index.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Motorcycle, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'main/post.html', context=context)


def show_category(request, cat_slug):
    cat = Category.objects.get(slug=cat_slug)
    posts = Motorcycle.objects.filter(cat_id=cat.id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': posts,
        'cat_selected': cat.id,
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    return render(request, 'main/about.html', {'title': 'О сайте', 'menu': menu})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    return render(request, 'main/addpage.html', {'form': form, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')