from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", include("tasks_app.urls", namespace="tasks")),
    path("users/", include("users.urls", namespace="users")),
]
