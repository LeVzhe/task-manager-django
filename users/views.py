from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from users.forms import UserLoginForm


def index(request):
    return render(request, "users/users.html")


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("users:index")
