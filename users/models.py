from django.contrib.auth.models import AbstractUser
from django.db import models

from tasks_app.models import WorkField


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)
    work_field = models.ManyToManyField(
        to=WorkField,
        through="WorkFieldUser",
        verbose_name="Поле",
    )


class WorkFieldUser(models.Model):
    work_field = models.ForeignKey(
        WorkField,
        on_delete=models.CASCADE,
        verbose_name="Поле",
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
