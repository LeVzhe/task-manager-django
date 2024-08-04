from django.urls import path

from tasks_app.views import TasksListView


app_name = "tasks"  # поле обязательное

urlpatterns = [
    path("", TasksListView.as_view(), name="tasks"),
]
