# views imports
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from task_manager.common.views import TitleMixin

# self imports
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import User


class UserLoginView(TitleMixin, LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("users:index")
    title = "Task Manager :: Логин"


class UserRegistrationView(TitleMixin, CreateView):
    model = User
    template_name = "users/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:login")
    success_message = "Регистрация прошла успешно!"
    title = "Task Manager :: Регистрация"


class UserProfileView(TitleMixin, UpdateView):
    model = User
    template_name = "users/profile.html"
    form_class = UserProfileForm
    title = "Task Manager :: Профиль"

    # Перенаправление после успешного обновления профиля
    def get_success_url(self):
        return reverse_lazy("users:profile", args=(self.object.id,))
