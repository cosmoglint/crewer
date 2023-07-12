import json
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.http import Http404
from django.db.models import Q, Count
from TaskManager.models import Task
from Auth.models import User
from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsManager
from .constants import ALL_RESOURCES_OCCUPIED

def project_list(request):
    if request.user.is_authenticated:
        if request.user.role == settings.MANAGER:
            return HttpResponse("to-do: send a list of projects")
        elif request.user.role == settings.MEMBER:
            return redirect(settings.TASK_TRACKER_URL)
        else:
            return HttpResponse('Unauthorized', status=401)
    else:
        return HttpResponse('Unauthorized', status=401)

def check_resources_and_assign(task, resources):
    required_skills = task.skills.all()
    # q_required_skills = [Q(skills=obj) for obj in required_skills]
    # skilled_users = resources.filter(Q(*q_required_skills, _connector=Q.AND))
    skilled_users = resources.filter(skills__in=required_skills).annotate(num_skills=Count('skills')).filter(num_skills=len(required_skills))
    task_assigned = False
    for skilled_user in skilled_users:
        success, reason = task.assign(skilled_user)
        if success:
            task_assigned = True
            break
    if not(task_assigned):
        reason = ALL_RESOURCES_OCCUPIED

    return task_assigned, reason

def allocate_tasks(request, project):
    # gets all the unassigned tasks for a project and assigns them to available resources
    request_user = request.user
    assignment_success_list = []
    assignment_failure_list = []
    if request_user.is_authenticated and request_user.role == settings.MANAGER:
        unassigned_project_tasks = Task.objects.prefetch_related('skills').filter(project=project, status=settings.UNASSIGNED)
        resources = User.objects.filter(role=settings.MEMBER)
        for task in unassigned_project_tasks:
            assigned, reason = check_resources_and_assign(task, resources)
            response = {
                'task': task.name,
                'reason': reason,
                'success': assigned
            }
            if assigned:
                assignment_success_list.append(response)
            else:
                assignment_failure_list.append(response)
        assignment_response = {
            'success': json.dumps(assignment_success_list),
            'failed': json.dumps(assignment_failure_list)
        }
        return JsonResponse(assignment_response)
    else:
        return HttpResponse("unauthorized", status=401)


class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticated, IsManager]
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):
    permission_classes = [permissions.IsAuthenticated, IsManager]
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)