from django.db import models
from apps.users.models import CustomUser
from apps.groups.models import Group

# CHOICES


class HomeworkStatus(models.TextChoices):
    PENDING_VERIFICATION = "Pending verification"
    COMPLETED = "Completed"
    WRONG = "Wrong"

# MODELS


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

    def __str__(self):
        return f"Homework {self.connection_with_task.task_name} by {self.author.username}"


class TaskComment(models.Model):
    text = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, related_name="comment")
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="comment")

    def __str__(self):
        return f"Comment to {self.task} by {self.author.username}"


class HomeworkComment(models.Model):
    text = models.TextField()
    homework = models.ForeignKey(Homework, on_delete=models.SET_NULL, null=True, related_name="comment")
