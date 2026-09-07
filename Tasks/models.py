from django.db import models
from django.contrib.auth.models import User

class TaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task_name = models.CharField(max_length=256)
    task_priority = models.CharField(max_length=30)
    task_status = models.BooleanField(default=False)
    task_added_at = models.DateTimeField(auto_now_add=True)
    task_description = models.TextField(default='Add Task Description here')