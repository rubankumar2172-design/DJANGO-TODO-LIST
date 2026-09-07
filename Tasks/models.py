from django.db import models
from django.contrib.auth.models import User

class TaskModel(models.Model):
    PRIORITY_CHOICES = [
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High'),
        ]
    TASK_STATUS_CHOICES = [
        ('Pending','Pending'),
        ('Completed','Completed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task_name = models.CharField(max_length=256)
    task_priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, default='Medium')
    task_status = models.CharField(max_length=30,choices=TASK_STATUS_CHOICES,default='Pending')
    task_added_at = models.DateTimeField(auto_now_add=True)
    task_description = models.TextField(default='Add Task Description here')