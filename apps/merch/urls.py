from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()


router.register(r"shop", MerchModelViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("merch-list/", MerchApiView.as_view()),
    path("merch-list/<int:pk>/", MerchApiView.as_view()),
    path("purchase-list/", ShoppingCartApiView.as_view()),
    path("purchase-list/<int:pk>/", ShoppingCartApiView.as_view())
]
