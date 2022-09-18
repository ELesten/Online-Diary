from .serializers import *


def role_check(self, request, serializer_class):
    """
    Function that generates a queryset based on the user's role.
    """
    if serializer_class == TaskSerializer and request.user.role == "Student":
        queryset = self.filter_queryset(
            self.get_queryset().filter(
                responsible_group=request.user.group
            )
        )
    elif serializer_class == TaskSerializer and request.user.role == "Teacher":
        queryset = self.filter_queryset(
            self.get_queryset().filter(
                responsible_group__in=request.user.lead_groups.values("id")
            )
        )
    elif serializer_class == TaskCommentSerializer and request.user.role == "Student":
        queryset = self.filter_queryset(
            self.get_queryset().filter(
                task__responsible_group=request.user.group
            )
        )
    elif serializer_class == TaskCommentSerializer and request.user.role == "Teacher":
        queryset = self.filter_queryset(
            self.get_queryset().filter(
                task__responsible_group__in=request.user.lead_groups.values("id")
            )
        )
    else:
        queryset = self.filter_queryset(self.get_queryset())
    return queryset
