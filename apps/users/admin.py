from django.contrib import admin
from .models import *
from ..homeworks.models import Homework, HomeworkComment
from ..merch.models import ShoppingCart
from ..tasks.models import TaskComment
from django.contrib.auth.admin import UserAdmin


class HomeworkInline(admin.TabularInline):
    model = Homework


class HomeworkCommentInline(admin.TabularInline):
    model = HomeworkComment


class ShoppingCartInline(admin.TabularInline):
    model = ShoppingCart


class TaskCommentInline(admin.TabularInline):
    model = TaskComment


class AdminCustomUser(UserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
                'first_name',
                'last_name',
                'email',
                'is_staff',
                'is_active',
                'is_superuser',
                'date_joined',
                'status',
                'role',
                'currency',
                'group',
            )
        }),
    )

    inlines = [
        HomeworkInline,
        HomeworkCommentInline,
        ShoppingCartInline,
        TaskCommentInline
    ]


admin.site.register(CustomUser, AdminCustomUser)
