from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.groups.models import Group

# CHOICES


class UserRole(models.TextChoices):
    STUDENT = "Student"
    TEACHER = "Teacher"
    MANAGER = "Manager"


class UserStatus(models.TextChoices):
    ACTIVE = "Active"
    VACATION = "Vacation"
    EXPELLED = "Expelled"


# MODELS


class CustomUser(AbstractUser):
    status = models.CharField(max_length=10, choices=UserStatus.choices, default=UserStatus.ACTIVE)
    role = models.CharField(
        max_length=10,
        choices=UserRole.choices,
        default=UserRole.STUDENT
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, related_name="student", null=True, blank=True
    )
    currency = models.IntegerField(null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
