from django.urls import path

from tasks_app.views import TasksListView, AddFieldFormView


app_name = "tasks"  # поле обязательное

urlpatterns = [
    path("", TasksListView.as_view(), name="tasks"),
    path("add_field/", AddFieldFormView.as_view(), name="add_field"),
]
