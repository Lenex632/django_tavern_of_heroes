from django.urls import path

from . import views_hero, views_items

app_name = 'app'

urlpatterns = [
    path("", views_hero.tavern, name="tavern"),
    path("create_hero/", views_hero.create_hero, name="create_hero"),
    path("<int:hero_id>/", views_hero.hero_ditail, name="hero_ditail"),
    path("<int:hero_id>/level_up/", views_hero.level_up, name="level_up"),
    path("<int:hero_id>/delete_hero/", views_hero.delete_hero, name="delete_hero"),
    path("<int:hero_id>/<int:item_id>/", views_hero.hero_item_detail, name="hero_item_detail"),
    path(
        "<int:hero_id>/<int:item_id>/remove_item_from_inventory",
        views_hero.remove_item_from_inventory,
        name="remove_item_from_inventory"
    ),

    path("items_list/", views_items.items_list, name="items_list"),
    path("items_list/create_item/", views_items.create_item, name="create_item"),
    path("items_list/<int:item_id>", views_items.item_ditail, name="item_ditail"),
    path("items_list/<int:item_id>/delete_item/", views_items.delete_item, name="delete_item"),
    path(
        "items_list/<int:item_id>/give_item_to_hero/",
        views_items.give_item_to_hero,
        name="give_item_to_hero"
    ),
]
