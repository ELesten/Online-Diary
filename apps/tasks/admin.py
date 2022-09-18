from django.contrib import admin
from .models import *


admin.site.register(Task)
admin.site.register(Homework)
admin.site.register(TaskComment)
admin.site.register(HomeworkComment)
