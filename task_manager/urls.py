from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from tasks_app.views import IndexClassView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexClassView.as_view(), name="index"),
    path("tasks/", include("tasks_app.urls", namespace="tasks")),
    path("users/", include("users.urls", namespace="users")),
]

if settings.DEBUG:
    urlpatterns.append(path("__debug__", include("debug_toolbar.urls")))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
