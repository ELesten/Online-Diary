from django.db import models
from django.contrib.auth.models import AbstractUser

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
    role = models.CharField(max_length=10, choices=UserRole.choices, blank=True, null=True)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
