from django.urls import path, include


routes = [
    path("task/", include("apps.tasks.urls")),
    path("user/", include("apps.users.urls")),
    path("homework/", include("apps.homeworks.urls")),
    path("group/", include("apps.groups.urls")),
]
