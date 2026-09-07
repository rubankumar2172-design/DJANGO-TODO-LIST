from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.forms import ModelForm

class SignupForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'})
    )

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control p-3',
            'placeholder': 'Enter username'
        }),max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control p-3',
            'placeholder': 'Enter password'
        }))

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['task_name', 'task_priority', 'task_status', 'task_description']
        widgets = {
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'task_status': forms.Select(attrs={'class': 'form-select'}),
        }

class TaskFilterForm(forms.Form):
    task_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by name'}))
    task_status = forms.ChoiceField(required=False, choices=[('', 'All')] + TaskModel.TASK_STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    task_priority = forms.ChoiceField(required=False, choices=[('', 'All')] + TaskModel.PRIORITY_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    task_description = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search in description'}))
    task_added_at = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime'}))