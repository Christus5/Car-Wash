from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from users.forms import *


def register_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('washapp:index')

    register_form = AccountRegisterForm()

    if request.method == 'POST':
        register_form = AccountRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect(settings.LOGIN_URL)

    return render(request, 'users/register.html', {
        'register_form': register_form
    })


def login_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('washapp:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('washapp:index')

    return render(request, 'users/login.html', {})


def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect(settings.LOGIN_URL)


class PasswordResetView(auth_views.PasswordResetView):
    success_url = reverse_lazy('users:password_reset_done')


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy('users:password_reset_complete')
