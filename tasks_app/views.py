from django.views.generic import TemplateView
from django.views.generic import ListView

from task_manager.common.views import TitleMixin
from tasks_app.models import WorkField  # , WorkFieldTask


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
