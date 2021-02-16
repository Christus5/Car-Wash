from django.shortcuts import render

from users.forms import *


def register_view(request, *args, **kwargs):
    register_form = AccountRegisterForm()
    return render(request, 'users/register.html', {
        'register_form': register_form
    })


def login_view(request, *args, **kwargs):
    login_form = AccountLoginForm()

    return render(request, 'users/login.html', {
        'login_form': login_form
    })
