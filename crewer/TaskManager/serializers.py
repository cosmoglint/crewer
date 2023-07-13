from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Task, Skill

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'project', 'assignee', 'skills', 'status', 'effort_estimate', 'start_date', 'end_date']

class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']

class SkillSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, 
        validators = [
            UniqueValidator(
                queryset=Skill.objects.all(),
            )
        ])

    class Meta:
        model = Skill
        fields = ['id', 'name', 'description']
