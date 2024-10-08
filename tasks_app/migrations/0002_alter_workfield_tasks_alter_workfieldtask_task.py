# Generated by Django 5.0.7 on 2024-08-07 22:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workfield',
            name='tasks',
            field=models.ManyToManyField(related_name='tasks', through='tasks_app.WorkFieldTask', to='tasks_app.task', verbose_name='Задачи'),
        ),
        migrations.AlterField(
            model_name='workfieldtask',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks_app.task', verbose_name='Задача'),
        ),
    ]
