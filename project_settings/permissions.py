from rest_framework import permissions

school_representatives = ["Teacher", "Manager"]


class IsAdminOrManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == "Manager" or request.user.is_staff)


class IsSchoolRepresentativeOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return bool(
                request.method in permissions.SAFE_METHODS
                and request.user.role == "Student"
                or request.user.role in school_representatives
            )
        return False


class IsSchoolRepresentative(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role in school_representatives)
