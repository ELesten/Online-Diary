from django.urls import path, include

routes = [
    path("user/", include("users.urls")),
]
