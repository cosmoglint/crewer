from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from .models import Task, Skill
from .serializers import TaskSerializer, SkillSerializer
from ProjectManager.permissions import IsManager, IsManagerOrReadonly
from .permissions import IsOwner


class TaskList(APIView):
    '''
    list view of all tasks of all projects
    managers can view all tasks
    resources can view all assigned tasks
    '''
    permission_classes = [permissions.IsAuthenticated, IsManagerOrReadonly]
    def get(self, request, format=None):
        request_user = request.user
        if request_user.is_manager():
            tasks = Task.objects.all()
        else:
            tasks = Task.objects.filter(assignee=request_user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    '''
    Detailed view of a specific Task with crud apis
    Managers can view and update all tasks
    Assignees can only view assigned tasks
    '''
    permission_classes = [permissions.IsAuthenticated, IsManagerOrReadonly, IsOwner]
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = TaskSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = TaskSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SkillList(APIView):
    '''
    list view of all skills. authorized users can view, add skills
    '''
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SkillSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SkillDetail(APIView):
    '''
    detailed view of a particular skill. authorized users can view skills
    managers can view, update and delete skills
    '''
    permission_classes = [permissions.IsAuthenticated, IsManager]
    def get_object(self, pk):
        try:
            return Skill.objects.get(pk=pk)
        except Skill.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        skill = self.get_object(pk)
        serializer = SkillSerializer(skill)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        skill = self.get_object(pk)
        serializer = SkillSerializer(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        skill = self.get_object(pk)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
