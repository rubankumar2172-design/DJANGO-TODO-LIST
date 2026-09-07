from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.forms import ModelForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['task_name', 'task_priority', 'task_status', 'task_description']
        widgets = {
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'task_status': forms.Select(attrs={'class': 'form-select'}),
        }