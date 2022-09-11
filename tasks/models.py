from django.db import models
from users.models import CustomUser
from groups.models import Group

# CHOICES


class HomeworkStatus(models.TextChoices):
    PENDING_VERIFICATION = "Pending verification"
    COMPLETED = "Completed"
    NOT_SATISFIED = "Wrong"

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
    responsible_group = models.ManyToManyField(Group, related_name="task", blank=True)

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
