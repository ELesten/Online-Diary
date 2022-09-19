from rest_framework import serializers
from .models import *


class HomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homework
        fields = "__all__"


class StudentHomeworkSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Homework
        fields = ["connection_with_task", "description", "links", "author", "id"] ## Убрать поле "id" после успешных тестов