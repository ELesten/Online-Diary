from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"tasks", TaskModelViewSet)
router.register(r"homework", HomeworkModelViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("my-homework/", StudentHomeworkListApiView.as_view()),
    path("my-homework/<int:pk>/", StudentHomeworkDetailApiView.as_view()),


]
