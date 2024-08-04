from django.db import models


class Task(models.Model):
    pass


class WorkField(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE, verbose_name="Задача")

    class Meta:
        verbose_name = "Поле"
        verbose_name_plural = "Поля"

    def __str__(self):
        return self.name
