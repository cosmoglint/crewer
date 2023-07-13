from rest_framework import permissions
from .models import Task


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if ( Task.objects.get(id=view.kwargs['pk']).assignee == request.user or request.user.is_manager()):
            return True
        else:
            return False