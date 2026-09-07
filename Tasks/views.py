from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import *
from .models import *


def Home_View(request):
    return render(request, 'home.html')

def Base_View(request):
    return render(request, 'base.html')

def Signup_View(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
    else:
        form = SignupForm()

    return render (request, 'signup.html',{'form':form})

def Login_View(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request,user)
                return redirect ('home')
    else:
        form = LoginForm()

    return render (request,'login.html',{'form':form})

def Logout_View(request):
    logout(request)
    return redirect ('home')

class TaskListView(ListView):
    model = TaskModel
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        # Restrict queryset to the current user
        queryset = TaskModel.objects.filter(user=self.request.user)
        form = TaskFilterForm(self.request.GET)

        if form.is_valid():
            data = form.cleaned_data
            if data.get('task_name'):
                queryset = queryset.filter(task_name__icontains=data['task_name'])
            if data.get('task_status'):
                queryset = queryset.filter(task_status=data['task_status'])
            if data.get('task_priority'):
                queryset = queryset.filter(task_priority=data['task_priority'])
            if data.get('task_description'):
                queryset = queryset.filter(task_description__icontains=data['task_description'])
            if data.get('task_added_at'):
                queryset = queryset.filter(task_added_at__date=data['task_added_at'])

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = TaskFilterForm(self.request.GET)
        return context

class TaskCreate_View(CreateView):
    model = TaskModel
    template_name = 'task_create.html'
    fields = ['task_name', 'task_priority', 'task_status', 'task_description']
    context_object_name = 'task_create'
    success_url = reverse_lazy(('task-list'))
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate_View(UpdateView):
    model = TaskModel
    template_name = 'task_create.html'
    fields = "__all__"
    context_object_name = 'task_update'
    success_url = reverse_lazy(('task-list'))

class TaskDelete_View(DeleteView):
    model = TaskModel
    template_name = 'task_delete.html'
    fields = "__all__"
    context_object_name = 'task_delete'
    success_url = reverse_lazy(('task-list'))

def TaskCompleted_View(request):
    tasks = TaskModel.objects.filter(task_status=True)
    return render (request,'task_completed.html',{'tasks':tasks})