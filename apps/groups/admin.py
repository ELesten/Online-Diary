from django.contrib import admin
from .models import *
from ..lessons.models import Lesson
from ..tasks.models import Task
from ..users.models import CustomUser


class LessonInline(admin.TabularInline):
    model = Lesson
    fields = [
        'lesson_name',
        'lesson_status',
        'record_download_link',
        'event_date',
    ]


class TaskInline(admin.TabularInline):
    model = Task
    fields = [
        'task_name',
        'created_by',
        'deadline',
    ]


class UserInline(admin.TabularInline):
    model = CustomUser
    fields = [
        'first_name',
        'last_name',
        'email',
        'status',
        'role',
        'currency',
    ]


class AdminGroup(admin.ModelAdmin):
    inlines = [
        LessonInline,
        TaskInline,
        UserInline
    ]


admin.site.register(Group, AdminGroup)
