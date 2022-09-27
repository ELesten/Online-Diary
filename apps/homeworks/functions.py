def homework_role_check(self, request):
    """
    Function that generates a queryset based on the user's role.
    """
    if request.user.role == "Teacher":
        queryset = self.filter_queryset(
            self.get_queryset().filter(
                connection_with_task__responsible_group__in=request.user.lead_groups.values("id")
            )
        )
    else:
        queryset = self.filter_queryset(self.get_queryset())

    return queryset
