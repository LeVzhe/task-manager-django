from django.urls import path

from tasks_app.views import (
    AddFieldCreateView,
    TasksListView,
    field_remove,
    AddTaskCreateView,
)

app_name = "tasks"  # поле обязательное

urlpatterns = [
    path("", TasksListView.as_view(), name="tasks_list"),
    path("add_field/", AddFieldCreateView.as_view(), name="add_field"),
    path("delete/<int:field_id>/", field_remove, name="delete_field"),
    path("add_task/", AddTaskCreateView.as_view(), name="add_task"),
]
