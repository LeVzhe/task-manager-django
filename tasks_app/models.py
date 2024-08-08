from django.db import models


class Task(models.Model):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    CRITICAL = 3
    STATUSES = (
        (LOW, "Низкий"),
        (MEDIUM, "Средний"),
        (HIGH, "Высокий"),
        (CRITICAL, "Критический"),
    )

    content = models.CharField(
        max_length=256, unique=False, verbose_name="Содержание", blank=True, null=True
    )
    piority_status = models.SmallIntegerField(default=LOW, choices=STATUSES)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class WorkField(models.Model):
    name = models.CharField(max_length=128, unique=False, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )
    tasks = models.ManyToManyField(
        to=Task,
        through="WorkFieldTask",
        verbose_name="Задачи",
        related_name="tasks",
    )

    class Meta:
        verbose_name = "Поле"
        verbose_name_plural = "Поля"

    def __str__(self):
        return self.name


class WorkFieldTask(models.Model):
    work_field = models.ForeignKey(
        WorkField, on_delete=models.CASCADE, verbose_name="Поле"
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
