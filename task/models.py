from django.db import models

class User(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=10)

class Task(models.Model):
    name = models.CharField(max_length=225)
    description  = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=100)
    completed_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100)
    user = models.ManyToManyField('User', related_name='tasks', blank=True)