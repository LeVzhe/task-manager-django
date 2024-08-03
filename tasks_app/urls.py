from django.urls import path

from tasks_app.views import index

app_name = "tasks"  # поле обязательное

urlpatterns = [
    path("", index, name="index"),
]
