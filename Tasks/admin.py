from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_name','task_priority','task_status','task_added_at','task_description','user']
    list_filter = ['task_name','task_priority','task_status','task_added_at','task_description','user']

admin.site.register(TaskModel,TaskAdmin)