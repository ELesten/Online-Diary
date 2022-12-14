from django.db.models import Q
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .functions import homework_role_check
from .serializers import *
from project_settings.permissions import *


class HomeworkModelViewSet(ModelViewSet):
    """
    CRUD to work with homeworks by the managers/teachers.
    """
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
    permission_classes = [IsSchoolRepresentative]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = [
        'homework_status',
        'connection_with_task'
    ]
    search_fields = [
        'author__username',
    ]
    ordering_fields = [
        'homework_status',
    ]

    def list(self, request, *args, **kwargs):
        queryset = homework_role_check(self, request)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class HomeworkCommentModelViewSet(ModelViewSet):
    """
    CRUD to work with homework comments by the managers/teachers.
    """
    serializer_class = HomeworkCommentSerializer
    queryset = HomeworkComment.objects.all()
    permission_classes = [IsSchoolRepresentative]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = [
        'homework__connection_with_task',
    ]
    search_fields = [
        'author__username',
    ]
    ordering_fields = [
        'author',
    ]


class StudentHomeworkApiView(APIView):
    """
    CRUD for student to getting all homeworks associated with him
    and a detailed modification of each of them.
    """
    serializer_class = StudentHomeworkSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            serializer = self.serializer_class(
                get_object_or_404(
                    Homework.objects.filter(author=request.user.id), pk=pk)
            )
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = self.serializer_class(
            Homework.objects.filter(author=request.user.id), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        user_group = Task.objects.filter(responsible_group=request.user.group).values_list("id", flat=True)
        if int(request.data.get("connection_with_task")) not in user_group:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(context={'request': request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        instance = get_object_or_404(
            Homework.objects.filter(author=request.user.id),
            pk=pk
        )
        serializer = self.serializer_class(
            instance, context={'request': request},
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        instance = get_object_or_404(Homework.objects.filter(author=request.user.id), pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HomeworkCommentApiView(APIView):
    """
    CRUD to work with homework comments by the managers/teachers.
    Students only have permissions to safe methods.
    """
    serializer_class = HomeworkCommentSerializer
    permission_classes = [IsSchoolRepresentativeOrReadOnly]

    def get(self, request, pk):
        serializer = self.serializer_class(
            get_object_or_404(
                HomeworkComment.objects.filter(
                    Q(homework=pk) & Q(homework__author=request.user.id) |
                    Q(homework=pk) & Q(author=request.user.id)
                )
            )
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        serializer = self.serializer_class(context={'request': request}, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        instance = get_object_or_404(
            HomeworkComment.objects.filter(Q(author=request.user.id) & Q(homework=pk))
        )
        serializer = self.serializer_class(
            instance, context={'request': request},
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        instance = get_object_or_404(
            HomeworkComment.objects.filter(Q(author=request.user.id) & Q(homework=pk))
        )
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
