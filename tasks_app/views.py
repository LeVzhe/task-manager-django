from django.views.generic import TemplateView

from task_manager.common.views import TitleMixin


class IndexClassView(TitleMixin, TemplateView):
    template_name = "tasks_app/index.html"
    title = "Task Manager :: Главная"
