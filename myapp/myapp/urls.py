from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("tavern_of_heroes.urls")),
    path("admin/", admin.site.urls),
]
