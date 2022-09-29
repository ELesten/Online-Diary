from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from project_settings.permissions import *
from rest_framework.permissions import IsAuthenticated
from .functions import task_comment_role_check, task_role_check


class TaskModelViewSet(ModelViewSet):
    """
    CRUD to work with tasks by the managers/teachers.
    Students only have permissions to safe methods.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [
        IsSchoolRepresentativeOrReadOnly,
    ]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = [
        'task_name',
        'created_by',
        'responsible_group'
    ]
    search_fields = [
        'task_name',
        'responsible_group__group_name',
    ]
    ordering_fields = [
        'deadline',
    ]


    def list(self, request, *args, **kwargs):
        queryset = task_role_check(self, request)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TaskCommentModelViewSet(ModelViewSet):
    """
    CRUD to work with task comments by the users.
    """
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer
    permission_classes = [
        IsAuthenticated
    ]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = [
        'task',
        'author',
    ]
    search_fields = [
        'task__task_name',
        'author',
    ]
    ordering_fields = [
        'task',
    ]

    def create(self, request, *args, **kwargs):
        user_group = Task.objects.filter(responsible_group=request.user.group).values_list("id", flat=True)
        if int(request.data.get("task")) not in user_group:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = task_comment_role_check(self, request)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author.username != request.user.username and request.user.role != "Manager":
            return Response(status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if instance.author.username != request.user.username and request.user.role != "Manager":
            return Response(status=status.HTTP_400_BAD_REQUEST)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data, status=status.HTTP_200_OK)

