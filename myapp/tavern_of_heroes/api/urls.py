from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('heroes_list/', views.HeroesListView.as_view(), name='heroes_list'),
    path('heroes_list/create_hero/', views.CreateHeroView.as_view(), name='create_hero'),
    path('heroes_list/<pk>/', views.HeroDetailView.as_view(), name='hero_detail'),

    path('items_list/', views.ItemsListView.as_view(), name='items_list'),
    path('items_list/<pk>', views.ItemsDetailView.as_view(), name='items_detail'),
]
