from django.urls import path

from users.views import index

app_name = "users"  # поле обязательное

urlpatterns = [
    path("", index, name="index"),
]
