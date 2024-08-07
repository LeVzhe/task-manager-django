from django.urls import path

from tasks_app.views import TasksListView, AddFieldCreateView


app_name = "tasks"  # поле обязательное

urlpatterns = [
    path("", TasksListView.as_view(), name="tasks_list"),
    path("add_field/", AddFieldCreateView.as_view(), name="add_field"),
]
