from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:hero_id>/", views.description, name="description"),
    path("<int:hero_id>/hero_class/", views.hero_class, name="hero_class"),
    path("<int:hero_id>/level_up/", views.level_up, name="level_up"),
]
