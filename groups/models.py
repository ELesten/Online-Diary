from django.db import models

# CHOICES


class UserRole(models.TextChoices):
    STUDENT = "Student"
    TEACHER = "Teacher"
    MANAGER = "Manager"


class GroupStatus(models.TextChoices):
    ACTIVE = "Active"
    DIPLOMA = "Diploma"
    BREAK = "Break"
    ISSUED = "Issued"
    PREPARING = "Preparing"


# MODELS


class Group(models.Model):
    group_name = models.CharField(max_length=255)
    teacher = models.ForeignKey(
        "users.CustomUser",
        related_name="lead_groups",
        limit_choices_to={"role": UserRole.TEACHER},
        on_delete=models.SET_NULL,
        null=True,
    )
    group_status = models.CharField(
        max_length=255, choices=GroupStatus.choices, default=GroupStatus.PREPARING
    )

    def __str__(self):
        return self.group_name
