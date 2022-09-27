from rest_framework import serializers
from .models import *


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = "__all__"


class StudentHomeworkSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    homework_status = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Homework
        fields = [
            "connection_with_task",
            "description",
            "links",
            "author",
            "homework_status",
            "created_at"
        ]


class HomeworkCommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = HomeworkComment
        fields = "__all__"
