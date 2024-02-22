from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:hero_id>/", views.hero_ditail, name="hero_ditail"),
    path("items_list/", views.items_list, name="items_list"),
    path("items_list/<int:item_id>", views.item_ditail, name="item_ditail"),
    path("<int:hero_id>/level_up/", views.level_up, name="level_up"),
]
