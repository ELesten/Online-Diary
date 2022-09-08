from rest_framework import permissions


class IsAdminOrManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == "Manager" or request.user.is_staff)
