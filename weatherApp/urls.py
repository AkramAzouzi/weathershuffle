from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseNotFound


def handle_not_found(request):
    return HttpResponseNotFound()


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("meteo.urls")),
    path("favicon.ico", handle_not_found),
]
