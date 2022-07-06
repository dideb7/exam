from django import forms
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

  