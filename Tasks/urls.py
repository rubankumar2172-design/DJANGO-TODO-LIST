from django.urls import path
from .views import *


urlpatterns = [
    path('', Home_View , name='home'),
    path('base', Base_View , name='base'),
    path('signup', Signup_View, name='signup'),
    path('login', Login_View, name='login'),
    path('logout',Logout_View, name='logout'),
    path('task-create',TaskCreate_View.as_view(), name='task-create'),
    path('task-list',TaskListView.as_view(), name='task-list'),
    path('<int:pk>/task-update',TaskUpdate_View.as_view(), name='task-update'),
    path('<int:pk>/task-delete',TaskDelete_View.as_view(), name='task-delete'),
    path('task-completed',TaskCompleted_View,name='task-completed'),
]   