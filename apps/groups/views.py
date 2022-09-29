from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from project_settings.permissions import *
from .serializers import *


class GroupModelViewSet(ModelViewSet):
    """
    CRUD to work with groups by the managers/teachers.
    """
    serializer_class = GroupSerializer
    permission_classes = [
        IsAuthenticated,
        IsSchoolRepresentative
    ]
    queryset = Group.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = [
        'teacher',
        'group_status',
    ]
    search_fields = [
        'teacher__username',
        'group_name',
    ]
    ordering_fields = [
        'teacher',
        'group_status',
    ]


