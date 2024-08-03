from django.urls import path

from users.views import index, UserLoginView

app_name = "users"  # поле обязательное

urlpatterns = [
    path("", index, name="index"),
    path("login/", UserLoginView.as_view(), name="login"),
]
