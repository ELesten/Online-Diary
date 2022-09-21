from rest_framework import serializers
from .models import Merch


class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merch
        fields = "__all__"
