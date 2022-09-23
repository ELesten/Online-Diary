from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()


router.register(r"merch", MerchModelViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("merch-list/", MerchApiView.as_view()),
    path("merch-list/<int:pk>/", MerchApiView.as_view()),
    path("purchase-list/", PurchaseApiView.as_view()),
    path("purchase-list/<int:pk>/", PurchaseApiView.as_view())
]
