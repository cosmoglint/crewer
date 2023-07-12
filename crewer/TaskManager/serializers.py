from rest_framework import serializers
from .models import Task, Skill

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description', 'assignee', 'status', 'effort_estimate', 'start_date', 'end_date']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'description', 'proficiency']