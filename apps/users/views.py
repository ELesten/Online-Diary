from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import CustomUser
from project_settings.permissions import *
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated


class UsersModelViewSet(ModelViewSet):
    """
    CRUD to manually change the user by the managers/teachers.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminOrManager
        ]
