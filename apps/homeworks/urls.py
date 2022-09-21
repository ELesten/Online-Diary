from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()


router.register(r"homework-list", HomeworkModelViewSet)
router.register(r"homework-comment", HomeworkCommentModelViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("my-homework/", StudentHomeworkApiView.as_view()),
    path("my-homework/<int:pk>/", StudentHomeworkApiView.as_view()),
    path("my-homework-comment/", HomeworkCommentApiView.as_view()),
    path("my-homework-comment/<int:pk>/", HomeworkCommentApiView.as_view())
]
