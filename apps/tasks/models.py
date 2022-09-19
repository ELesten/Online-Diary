from django.db import models
from apps.users.models import CustomUser
from apps.groups.models import Group


class Task(models.Model):
    task_name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name="user_task"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    responsible_group = models.ForeignKey(Group, related_name="task", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.task_name


class TaskComment(models.Model):
    text = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, related_name="comment")
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="comment")

    def __str__(self):
        return f"Comment to {self.task} by {self.author.username}"
