from django.contrib import admin

from tasks_app.models import Task, WorkField


# Register your models here.
class WorkFieldAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_timestamp",
    )
    list_display_links = ("name", "description", "created_timestamp")


admin.site.register(WorkField, WorkFieldAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "piority_status",
    )
    list_display_links = ("content", "piority_status")


admin.site.register(Task, TaskAdmin)
