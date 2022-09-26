from rest_framework.viewsets import ModelViewSet
from project_settings.permissions import *
from .serializers import *


class GroupModelViewSet(ModelViewSet):
    """
    CRUD to work with groups by the managers/teachers.
    """
    serializer_class = GroupSerializer
    permission_classes = [IsSchoolRepresentative]
    queryset = Group.objects.all()
    filterset_fields = [
        "teacher",
        "group_status",
    ]


