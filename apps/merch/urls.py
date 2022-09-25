from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()


router.register(r"shop", MerchModelViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("purchase-list/", ShoppingCartApiView.as_view()),
    path("purchase-detail/<int:pk>/", ShoppingCartApiView.as_view())
]
