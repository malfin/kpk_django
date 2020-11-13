import django.contrib.auth as auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from authapp.forms import LoginForm, RegisterForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = LoginForm()
    content = {
        'page_title': 'Авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = RegisterForm()
    content = {
        'page_title': 'Регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', content)


def profile(request):
    context = {
        'page_title': 'Профиль',
    }
    return render(request, 'authapp/profile.html', context)
