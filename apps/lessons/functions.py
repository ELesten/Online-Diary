def lesson_role_check(self, request):
    """
    Function that generates a queryset based on the user's role.
    """
    if request.user.role == "Student":
        queryset = self.filter_queryset(
            self.get_queryset().filter(
                connection_with_group=request.user.group
            )
        )
    elif request.user.role == "Teacher":
        queryset = self.filter_queryset(
            self.get_queryset().filter(
                connection_with_group__in=request.user.lead_groups.values("id")
            )
        )
    else:
        queryset = self.filter_queryset(self.get_queryset())

    return queryset
