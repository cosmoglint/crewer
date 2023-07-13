from rest_framework import permissions
from django.conf import settings


class IsOwnerOrManager(permissions.BasePermission):
    """
    Check if user is a manager or accessing their own profile
    """

    def has_permission(self, request, view):
        print(view.kwargs)
        if request.user.is_manager():
            return True
        elif view.kwargs['id']==request.user.id:
            return True
        else:
            return False
