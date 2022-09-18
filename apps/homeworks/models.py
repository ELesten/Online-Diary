from django.db import models
from apps.users.models import CustomUser
from apps.tasks.models import Task
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

    def __str__(self):
        return f"Homework {self.connection_with_task.task_name} by {self.author.username}"


class HomeworkComment(models.Model):
    text = models.TextField()
    homework = models.ForeignKey(Homework, on_delete=models.SET_NULL, null=True, related_name="comment")