# Generated by Django 5.0.7 on 2024-08-08 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_app', '0004_remove_workfield_tasks_remove_workfieldtask_task_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workfield',
            name='tasks',
            field=models.ManyToManyField(related_name='tasks', through='tasks_app.WorkFieldTask', to='tasks_app.task', verbose_name='Задачи'),
        ),
        migrations.RemoveField(
            model_name='workfieldtask',
            name='task',
        ),
        migrations.RemoveField(
            model_name='workfieldtask',
            name='work_field',
        ),
        migrations.AddField(
            model_name='workfieldtask',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks_app.task', verbose_name='Задача'),
        ),
        migrations.AddField(
            model_name='workfieldtask',
            name='work_field',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='tasks_app.workfield', verbose_name='Поле'),
            preserve_default=False,
        ),
    ]
