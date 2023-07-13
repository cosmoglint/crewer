from rest_framework import permissions
from django.conf import settings


class IsManager(permissions.BasePermission):
    """
    Check if user is a manager and only allaw managers to create, edit, update projects
    """

    def has_permission(self, request, view):
        if request.user.is_manager():
            return True
        else:
            return False

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

class IsManagerOrReadonly(permissions.BasePermission):
    """
    allow all access to managers, only read access to others
    """
    def has_permission(self, request, view):
        if ( ( request.method in SAFE_METHODS ) or request.user.is_manager()):
            return True
        else:
            return False
