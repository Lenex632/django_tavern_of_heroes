from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
        user = User()
        user.username = request.POST['username']
        try:
            user.set_password(request.POST['password'])
            user.save()
            login(request, user)
            return redirect('app:tavern')
        except:
            messages.error(request, 'Плохой пароль')

    return render(request, 'tavern_of_heroes/login/registration.html')
