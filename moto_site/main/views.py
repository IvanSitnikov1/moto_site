from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import *
from .forms import *
from .utils import DataMixin, menu


# Вывод всех постов и постов по категориям
class MotorcycleHome(DataMixin, ListView):
    model = Motorcycle
    template_name = 'main/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return {**context, **c_def}

    def get_queryset(self):
        return Motorcycle.objects.filter(is_published=True)


class MotorcycleCategory(DataMixin, ListView):
    model = Motorcycle
    template_name = 'main/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Категория - ' + str(context['posts'][0].cat),
            cat_selected=context['posts'][0].cat_id
        )
        return {**context, **c_def}

    def get_queryset(self):
        return Motorcycle.objects.filter(
            cat__slug=self.kwargs['cat_slug'],
            is_published=True
        )


# GRUD операции с постами
class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'main/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return {**context, **c_def}

    def form_valid(self, form):
        post = form.save(commit=False)
        author = self.request.user.username
        post.author = author
        post.save()
        return redirect(f'/post/{post.slug}')


class ShowPost(DataMixin, DetailView):
    model = Motorcycle
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return {**context, **c_def}


class UpdatePost(DataMixin, UpdateView):
    model = Motorcycle
    form_class = AddPostForm
    template_name = 'main/update_post.html'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Редактирование поста')
        return {**context, **c_def}


def delete(request, post_slug):
    post = Motorcycle.objects.get(slug=post_slug)
    post.delete()
    return redirect(f'/category/{post.cat.slug}')


# Регистрация и авторизация пользователей
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return {**context, **c_def}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return {**context, **c_def}


def logout_user(request):
    logout(request)
    return redirect('login')


def about(request):
    cats = Category.objects.annotate(Count('motorcycle'))
    user_menu = menu.copy()
    if not request.user.is_authenticated:
        user_menu.pop(1)
    return render(
        request,
        'main/about.html',
        {'menu': user_menu, 'cats': cats}
    )


def contact(request):
    cats = Category.objects.annotate(Count('motorcycle'))
    user_menu = menu.copy()
    if not request.user.is_authenticated:
        user_menu.pop(1)
    return render(
        request,
        'main/contact.html',
        {'menu': user_menu, 'cats': cats}
    )


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
