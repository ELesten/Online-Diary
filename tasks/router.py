from django.urls import path, include

tasks_routes = [
    path("task/", include("tasks.urls")),
]
