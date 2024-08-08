from tasks_app.forms import WorkField


def work_field(request):
    return {"work_field": WorkField}
