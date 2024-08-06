from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from task_manager.common.views import TitleMixin
from tasks_app.models import WorkField
from tasks_app.forms import FieldAddForm


class IndexClassView(TitleMixin, TemplateView):
    template_name = "tasks_app/index.html"
    title = "Task Manager :: Главная"


class TasksListView(TitleMixin, ListView):
    template_name = "tasks_app/tasks.html"
    title = "Task Manager :: Рабочая область"
    context_object_name = "work_fields"
    ordering = "created_timestamp"

    def get_queryset(self):
        current_user = self.request.user
        queryset = WorkField.objects.filter(workfielduser__user=current_user).order_by(
            self.ordering
        )
        return queryset


class AddFieldFormView(TitleMixin, FormView):
    template_name = "tasks_app/add_field.html"
    form_class = FieldAddForm
    success_url = reverse_lazy("tasks:tasks")
    title = "Task Manager :: Добавить поле"
