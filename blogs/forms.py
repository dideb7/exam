from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class AddPF(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Article
        fields = ['title', 'content', 'photo', 'slug', 'cat']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 70, 'rows': 20})
        }


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'})
        }