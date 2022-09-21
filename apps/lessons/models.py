from django.db import models
from ..groups.models import Group

# CHOICES


class LessonStatus(models.TextChoices):
    CONDUCTED = "Conducted"
    NOT_CONDUCTED = "Not conducted"


# MODELS

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=255)
    lesson_status = models.CharField(choices=LessonStatus.choices, default=LessonStatus.NOT_CONDUCTED, max_length=255)
    description = models.TextField()
    record_download_link = models.URLField(null=True, blank=True)
    event_date = models.DateTimeField(null=True, blank=True)
    connection_with_group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name="lesson")

    def __str__(self):
        return self.lesson_name
