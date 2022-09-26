from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
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
