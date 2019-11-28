import requests
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import User
from django.middleware import csrf

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

def login(request):
    context = {}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user != None:
            auth.login(request, user)
            return redirect('/')
        else:
            context['login_error'] = "Введен не правильный логин или пароль"
            # return render_to_response('LoginApp/login.html', ctx)
    return render(request, 'LogsysApp/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect("/")

def registration(request):
    ctx = {}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        user_list = User.objects.all()
        bool_user = False
        for name in user_list:
            if name.username == username:
                bool_user = True
        if password != password2:
            ctx['login_error'] = "Пароли не совпадают"
        elif len(password) < 5:
            ctx['login_error'] = "Пароль слишком короткий"
        elif password == username:
            ctx['login_error'] = "Пароль не должен совпадать с логином"
        elif bool_user == True:
            ctx['login_error'] = "Логин уже существует"
        else:
            User.objects.create_user(username=username, password=password2)
            # user = auth.authenticate(username=username, password=password2)
            # auth.login(request, user)
            ctx['login_error'] = "Регистрация прошла успешно"
            return render(request, 'LogsysApp/login.html', ctx)

    return render(request, 'LogsysApp/registration.html', ctx)