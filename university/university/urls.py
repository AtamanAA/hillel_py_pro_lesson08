from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("student/", include("student.urls")),
    path("teacher/", include("teacher.urls")),
    # path("group/", include("group.urls")),
]
