from django.shortcuts import render


def index(request):
    return render(request, "tasks_app/tasks_app.html")
