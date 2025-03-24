from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=225)
    description  = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=100)
    completed_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100)
    
class User(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=10)
    tasks = models.ManyToManyField('Task', related_name='users', blank=True)