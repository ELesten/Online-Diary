from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from project_settings.permissions import IsSchoolRepresentative
from django.shortcuts import get_object_or_404


class MerchModelViewSet(ModelViewSet):
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer
    permission_classes = [IsSchoolRepresentative]


class MerchApiView(APIView):
    serializer_class = MerchSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            serializer = self.serializer_class(
                get_object_or_404(
                    Merch.objects.filter(id=pk)
                )
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.serializer_class(Merch.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PurchaseApiView(APIView):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            serializer = self.serializer_class(get_object_or_404(
                    Purchase.objects.filter(purchaser=request.user.id), pk=pk
                )
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.serializer_class(Purchase.objects.filter(purchaser=request.user.id), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(context={'request': request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = get_object_or_404(Purchase.objects.filter(purchaser=request.user.id), pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
