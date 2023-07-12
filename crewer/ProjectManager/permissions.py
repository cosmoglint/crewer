from rest_framework import permissions
from django.conf import settings


class IsManager(permissions.BasePermission):
    """
    Check if user is a manager and only allaw managers to create, edit, update projects
    """

    def has_permission(self, request, view):
        if request.user.role == settings.MANAGER:
            return True
        else:
            return False
