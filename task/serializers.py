from rest_framework import serializers
from .models import User, Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ("id", "name", "description", "created_at", "task_type", "status", "users")
        extra_kwargs = {'users': {'required': False}}

class UserSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "name", "email", "mobile", "tasks")
        extra_kwargs = {'tasks': {'required': False}}
