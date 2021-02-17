from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Account


class AccountRegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2')


class AccountLoginForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('username',)
