from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from project_settings.permissions import *


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