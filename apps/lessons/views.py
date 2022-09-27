from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .functions import lesson_role_check
from .models import Lesson
from .serializers import LessonSerializer
from project_settings.permissions import IsSchoolRepresentativeOrReadOnly


class LessonModelViewSet(ModelViewSet):
    """
    CRUD to work with lessons by the managers/teachers.
    Students only have permissions to safe methods.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsSchoolRepresentativeOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = [
        'lesson_status',
        'connection_with_group',
    ]
    search_fields = [
        'lesson_name',
    ]
    ordering_fields = [
        'lesson_status',
    ]

    def list(self, request, *args, **kwargs):
        queryset = lesson_role_check(self, request)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
