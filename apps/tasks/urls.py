from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"tasks", TaskModelViewSet)
router.register(r"task-comment", TaskCommentModelViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
