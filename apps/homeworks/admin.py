from django.contrib import admin
from .models import *


class CommentInline(admin.TabularInline):
    model = HomeworkComment


class AdminHomework(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]


admin.site.register(Homework, AdminHomework)
admin.site.register(HomeworkComment)
