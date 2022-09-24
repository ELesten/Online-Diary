from django.contrib import admin
from .models import *
from ..homeworks.models import Homework


class HomeworkInline(admin.TabularInline):
    model = Homework
    fields = [
        'links',
        'homework_status',
        'author'
    ]


class CommentInline(admin.TabularInline):
    model = TaskComment


class AdminTask(admin.ModelAdmin):
    inlines = [
        HomeworkInline,
        CommentInline
    ]


admin.site.register(Task, AdminTask)
admin.site.register(TaskComment)
