from django.contrib import admin
from .models import *
from ..homeworks.models import Homework, HomeworkComment
from ..merch.models import ShoppingCart
from ..tasks.models import TaskComment


class HomeworkInline(admin.TabularInline):
    model = Homework


class HomeworkCommentInline(admin.TabularInline):
    model = HomeworkComment


class ShoppingCartInline(admin.TabularInline):
    model = ShoppingCart


class TaskCommentInline(admin.TabularInline):
    model = TaskComment


class AdminCustomUser(admin.ModelAdmin):
    inlines = [
        HomeworkInline,
        HomeworkCommentInline,
        ShoppingCartInline,
        TaskCommentInline
    ]


admin.site.register(CustomUser, AdminCustomUser)
