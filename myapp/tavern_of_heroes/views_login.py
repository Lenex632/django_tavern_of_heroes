from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def sign_in(request) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app:tavern')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')

    return render(request, 'tavern_of_heroes/login/login.html')


def sign_out(request) -> HttpResponse:
    logout(request)
    return render(request, 'tavern_of_heroes/login/logout.html')


def registration(request) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, password=password)
            login(request, user)
            return redirect('app:tavern')
        except Exception as e:
            messages.error(request, f'Во время регистрации что-то пошло не так {e}')

    return render(request, 'tavern_of_heroes/login/registration.html')
