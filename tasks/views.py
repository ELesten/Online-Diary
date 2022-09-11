from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from project_settings.permissions import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class TaskModelViewSet(ModelViewSet):
    """
    CRUD to work with tasks by the managers/teachers.
    Students only have permissions to safe methods.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsSchoolRepresentativeOrReadOnly]


class HomeworkModelViewSet(ModelViewSet):
    """
    CRUD to work with homeworks by the managers/teachers.
    """
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
    permission_classes = [IsSchoolRepresentative]


class StudentHomeworkListApiView(APIView):
    serializer_class = StudentHomeworkSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.serializer_class(
            Homework.objects.filter(author=request.user.id),
            many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentHomeworkDetailApiView(APIView):
    serializer_class = StudentHomeworkSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        serializer = self.serializer_class(get_object_or_404(Homework, pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        instance = get_object_or_404(Homework, pk=pk)
        serializer = self.serializer_class(instance, context={'request': request}, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

