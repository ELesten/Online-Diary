from django.urls import path, include

users_routes = [
    path("user/", include("users.urls")),
]
