from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()


router.register(r"homework-list", HomeworkModelViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("my-homework/", StudentHomeworkListCreateApiView.as_view()),
    path("my-homework/<int:pk>/", StudentHomeworkDetailApiView.as_view()),
]
