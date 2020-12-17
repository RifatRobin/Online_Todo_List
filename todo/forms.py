from django import forms
from django.forms import ModelForm

from .models import *


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        exclude = ('creation_Time', 'user',)
