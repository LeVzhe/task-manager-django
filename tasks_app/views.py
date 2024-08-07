from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from task_manager.common.views import TitleMixin
from tasks_app.models import WorkField
from users.models import WorkFieldUser
from tasks_app.forms import FieldAddForm


class IndexClassView(TitleMixin, TemplateView):
    template_name = "tasks_app/index.html"
    title = "Task Manager :: Главная"


class TasksListView(TitleMixin, ListView):
    template_name = "tasks_app/tasks.html"
    title = "Task Manager :: Рабочая область"
    context_object_name = "work_fields"
    ordering = "-created_timestamp"

    def get_queryset(self):
        current_user = self.request.user
        queryset = WorkField.objects.filter(workfielduser__user=current_user).order_by(
            self.ordering
        )
        return queryset


class AddFieldCreateView(TitleMixin, CreateView):
    template_name = "tasks_app/add_field.html"
    model = WorkField
    form_class = FieldAddForm
    success_url = reverse_lazy("tasks:tasks_list")
    title = "Task Manager :: Добавить поле"
    success_message = "Поле успешно создано!"

    def form_valid(self, form):
        # Получаем текущего пользователя, который добавляет поле
        current_user = self.request.user

        # Создаем объект поля, но не сохраняем его в базе данных
        field_name = form.cleaned_data["name"]
        field_description = form.cleaned_data["description"]
        new_work_field = WorkField(name=field_name, description=field_description)
        new_work_field.save()
        work_field_user = WorkFieldUser(user=current_user, work_field=new_work_field)

        work_field_user.save()

        return super().form_valid(form)
