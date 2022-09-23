from rest_framework import serializers
from .models import Merch, Purchase


class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merch
        fields = "__all__"


class PurchaseSerializer(serializers.ModelSerializer):
    purchaser = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.ReadOnlyField()

    class Meta:
        model = Purchase
        fields = "__all__"
