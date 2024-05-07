from django.urls import path

from . import views_general, views_items, views_heroes

app_name = 'api'

urlpatterns = [
    path('', views_general.get_routes, name='index'),
    path('users/', views_general.UsersListView.as_view(), name='users_list'),
    path('users/create_user/', views_general.CreateUserView.as_view(), name='create_user'),
    path('users/<pk>/', views_general.UserDetailView.as_view(), name='user_detail'),
    path('users/<pk>/delete_user', views_general.DeleteUserView.as_view(), name='delete_user'),

    path('heroes_list/', views_heroes.HeroesListView.as_view(), name='heroes_list'),
    path('heroes_list/create_hero/', views_heroes.CreateHeroView.as_view(), name='create_hero'),
    path('heroes_list/<pk>/', views_heroes.HeroDetailView.as_view(), name='hero_detail'),
    path('heroes_list/<pk>/delete_hero', views_heroes.DeleteHeroView.as_view(), name='delete_hero'),
    path('heroes_list/<pk>/level_up', views_heroes.LevelUpHeroView.as_view(), name='level_up'),
    path('heroes_list/<pk>/inventory/remove_item/<item_id>', views_heroes.HeroRemoveItemView.as_view(), name='remove_item'),
    path('heroes_list/<pk>/inventory', views_heroes.HeroInventoryView.as_view(), name='inventory'),

    path('items_list/', views_items.ItemsListView.as_view(), name='items_list'),
    path('items_list/create_item', views_items.CreateItemsView.as_view(), name='create_item'),
    path('items_list/<pk>', views_items.ItemsDetailView.as_view(), name='items_detail'),
    path('items_list/<pk>/delete_item', views_items.DeleteItemView.as_view(), name='delete_item'),
    path('items_list/<pk>/give_item_to_hero/<hero_id>', views_items.GiveItemView.as_view(), name='give_item_to_hero'),
]
