from django.shortcuts import render


def index(request):
    context = {"title": "Task Manager :: Home"}
    return render(request, "tasks_app/tasks_app.html", context)
