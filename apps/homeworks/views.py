from django.shortcuts import render
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
