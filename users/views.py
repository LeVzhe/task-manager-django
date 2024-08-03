from django.shortcuts import render
from django.urls import reverse_lazy

# views imports
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

# self imports
from users.forms import UserLoginForm, UserRegistrationForm
from users.models import User


def index(request):
    return render(request, "users/users.html")


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("users:index")


class UserRegistrationView(CreateView):
    model = User
    template_name = "users/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:index")
    success_message = "Регистрация прошла успешно!"
