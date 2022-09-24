from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import CustomUser
from project_settings.permissions import *
from rest_framework.permissions import IsAuthenticated


class UsersModelViewSet(ModelViewSet):
    """
    CRUD to work with users by the managers.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsSchoolRepresentative,
    ]


class UserPasswordChange(APIView):
    """
    Endpoint to change password by the user.
    """
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        serializer = self.serializer_class(get_object_or_404(CustomUser.objects.filter(id=request.user.id)))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        instance = get_object_or_404(CustomUser.objects.filter(id=request.user.id))
        serializer = self.serializer_class(
            instance,
            context={'request': request},
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
