from django.shortcuts import render
from django.urls import reverse_lazy

# views imports
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView

# self imports
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User
from task_manager.common.views import TitleMixin


def index(request):
    return render(request, "users/users.html")


class UserLoginView(TitleMixin, LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("users:index")
    title = "Task Manager :: Логин"


class UserRegistrationView(TitleMixin, CreateView):
    model = User
    template_name = "users/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:index")
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
