from django.views.generic import TemplateView
from django.views.generic import ListView

from task_manager.common.views import TitleMixin
from tasks_app.models import WorkField  # , WorkFieldTask

from users.models import WorkFieldUser


class IndexClassView(TitleMixin, TemplateView):
    template_name = "tasks_app/index.html"
    title = "Task Manager :: Главная"


class TasksListView(TitleMixin, ListView):
    model = WorkField
    template_name = "tasks_app/tasks.html"
    title = "Task Manager :: Рабочая область"
    context_object_name = "work_fields"

    def get_queryset(self):
        current_user = self.request.user
        queryset = WorkFieldUser.objects.filter(user=current_user)
        return queryset
