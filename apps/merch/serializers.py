from rest_framework import serializers
from .models import ShoppingCart, MerchShop


class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchShop
        fields = "__all__"


class ShoppingCartSerializer(serializers.ModelSerializer):
    purchaser = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.ReadOnlyField()

    class Meta:
        model = ShoppingCart
        fields = "__all__"
