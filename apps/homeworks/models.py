from django.db import models
from rest_framework.generics import get_object_or_404
from django.db.models import F
from apps.users.models import CustomUser
from apps.tasks.models import Task
from django.db.models import signals
from django.dispatch import receiver

# CHOICES


class HomeworkStatus(models.TextChoices):
    PENDING_VERIFICATION = "Pending verification"
    COMPLETED = "Completed"
    WRONG = "Wrong"

# MODELS


class Homework(models.Model):
    connection_with_task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, related_name="homework")
    description = models.TextField()
    links = models.URLField(null=True)
    homework_status = models.CharField(
        max_length=255,
        choices=HomeworkStatus.choices,
        default=HomeworkStatus.PENDING_VERIFICATION
    )
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="homework")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Homework for the task {self.connection_with_task.task_name} by {self.author.username}"


class HomeworkComment(models.Model):
    text = models.TextField()
    homework = models.ForeignKey(Homework, on_delete=models.SET_NULL, null=True, related_name="comment")
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="homework_comment")

    def __str__(self):
        return f"Comment to homework № {self.homework.id} by {self.author.username}"
