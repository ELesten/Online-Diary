from django.urls import path, include


routes = [
    path("task/", include("apps.tasks.urls")),
    path("user/", include("apps.users.urls"))
]