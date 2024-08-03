from django.contrib import admin
from django.urls import path, include

from tasks_app.views import index


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("tasks/", include("tasks_app.urls", namespace="tasks")),
    path("users/", include("users.urls", namespace="users")),
]
