from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"users-list", UsersModelViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("drf-auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls")),
]
