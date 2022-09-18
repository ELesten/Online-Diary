from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from project_settings.permissions import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .functions import role_check


class TaskModelViewSet(ModelViewSet):
    """
    CRUD to work with tasks by the managers/teachers.
    Students only have permissions to safe methods.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsSchoolRepresentativeOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = role_check(self, request, serializer_class=TaskSerializer)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class HomeworkModelViewSet(ModelViewSet):
    """
    CRUD to work with homeworks by the managers/teachers.
    """
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
    permission_classes = [IsSchoolRepresentative]


class StudentHomeworkListCreateApiView(APIView):
    """
    Endpoint for student to getting all homeworks associated with him and
    create new homework.
    """
    serializer_class = StudentHomeworkSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.serializer_class(
            Homework.objects.filter(author=request.user.id),
            many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(context={'request': request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentHomeworkDetailApiView(APIView):
    """
    Endpoint for student to getting/change selected homework.
    """
    serializer_class = StudentHomeworkSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        serializer = self.serializer_class(
            get_object_or_404(
                Homework.objects.filter(author=request.user.id),
                pk=pk
            )
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

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


class TaskCommentModelViewSet(ModelViewSet):
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user_group = Task.objects.filter(responsible_group=request.user.group).values_list("id", flat=True)
        if int(request.data.get("task")) not in user_group:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = role_check(self, request, serializer_class=TaskCommentSerializer)

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

