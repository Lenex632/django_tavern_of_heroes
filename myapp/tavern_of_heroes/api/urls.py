from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('', views.get_routes, name='index'),

    path('heroes_list/', views.HeroesListView.as_view(), name='heroes_list'),
    path('heroes_list/create_hero/', views.CreateHeroView.as_view(), name='create_hero'),
    path('heroes_list/<pk>/', views.HeroDetailView.as_view(), name='hero_detail'),
    path('heroes_list/<pk>/delete_hero', views.DeleteHeroView.as_view(), name='delete_hero'),
    path('heroes_list/<pk>/level_up', views.LevelUpHeroView.as_view(), name='level_up'),
    path('heroes_list/<pk>/inventory/remove_item/<item_id>', views.HeroRemoveItemView.as_view(), name='remove_item'),
    path('heroes_list/<pk>/inventory', views.HeroInventoryView.as_view(), name='inventory'),

    path('items_list/', views.ItemsListView.as_view(), name='items_list'),
    path('items_list/create_item', views.CreateItemsView.as_view(), name='create_item'),
    path('items_list/<pk>', views.ItemsDetailView.as_view(), name='items_detail'),
    path('items_list/<pk>/delete_item', views.DeleteItemView.as_view(), name='delete_item'),
    path('items_list/<pk>/give_item_to_hero/<hero_id>', views.GiveItemView.as_view(), name='give_item_to_hero'),
]
