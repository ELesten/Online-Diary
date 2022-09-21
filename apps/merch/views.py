from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated


class MerchModelViewSet(ModelViewSet):
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer
    permission_classes = [IsAuthenticated]
