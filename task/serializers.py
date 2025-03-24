from rest_framework import serializers
from .models import User, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "email", "mobile", "tasks")
        extra_kwargs = {'tasks': {'required': False}}


class TaskSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ("id", "name", "description", "created_at", "task_type", "status", "users")
        extra_kwargs = {'users': {'required': False}}