from ..models import Item, Hero
from rest_framework import generics, decorators, response
from .serializers import HeroSerializer, ItemSerializer


@decorators.api_view(['GET'])
def get_routes(request):
    routes = [
        'GET /api',

        'Действия с героями',
        'GET /api/heroes_list - список героев',
        'POST /api/heroes_list/create_hero - создать героя',
        'GET /api/heroes_list/:hero_id - посмотреть детали героя hero_id',
        'DELETE /api/heroes_list/:hero_id/delete_hero - удалить героя hero_id',
        'PUT /api/heroes_list/:hero_id/level_up - поднять уровень герою hero_id',
        'GET /api/heroes_list/:hero_id/inventory - посмотреть инвентарь героя hero_id',
        'DELETE /api/heroes_list/:hero_id/remove_item/:item_id - удалить предмет item_id из инвентаря героя '
        'hero_id',

        'Действия с предметами',
        'GET /api/items_list - список всех предметов',
        'POST /api/items_list/create_item - создать предмет',
        'GET /api/items_list/:item_id - посмотреть описание предмета item_id',
        'DELETE /api/items_list/:item_id/delete_item - удалить предмет item_id',
        'PUT /api/items_list/:item_id/give_item_to_hero/:hero_id - дать предмет item_id герою hero_id',
    ]
    return response.Response(routes)


class HeroesListView(generics.ListAPIView):
    queryset = Hero.objects.all().order_by('id')
    serializer_class = HeroSerializer


class HeroDetailView(generics.RetrieveAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


class CreateHeroView(generics.CreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


class DeleteHeroView(generics.DestroyAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


class LevelUpHeroView(generics.UpdateAPIView):
    serializer_class = HeroSerializer

    def put(self, request, *args, **kwargs):
        hero = Hero.objects.get(pk=self.kwargs['pk'])
        hero.level_up()
        return response.Response(self.serializer_class(hero).data)

    def patch(self, request, *args, **kwargs):
        hero = Hero.objects.get(pk=self.kwargs['pk'])
        hero.level_up()
        return response.Response(self.serializer_class(hero).data)


class HeroInventoryView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        hero = Hero.objects.get(pk=self.kwargs['pk'])
        self.queryset = hero.list_of_items
        return self.list(request, *args, **kwargs)


class HeroRemoveItemView(generics.DestroyAPIView):
    serializer_class = ItemSerializer
    lookup_field = ['item_id']

    def delete(self, request, *args, **kwargs):
        hero = Hero.objects.get(pk=self.kwargs['pk'])
        item = Item.objects.get(pk=self.kwargs['item_id'])
        hero.list_of_items.remove(item)
        return response.Response(HeroSerializer(hero).data)


class ItemsListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemsDetailView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CreateItemsView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class DeleteItemView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class GiveItemView(generics.UpdateAPIView):
    serializer_class = HeroSerializer
    lookup_field = ['hero_id']

    def put(self, request, *args, **kwargs):
        hero = Hero.objects.get(pk=self.kwargs['hero_id'])
        item = Item.objects.get(pk=self.kwargs['pk'])
        hero.list_of_items.add(item)
        return response.Response(self.serializer_class(hero).data)

    def patch(self, request, *args, **kwargs):
        hero = Hero.objects.get(pk=self.kwargs['hero_id'])
        item = Item.objects.get(pk=self.kwargs['pk'])
        hero.list_of_items.add(item)
        return response.Response(self.serializer_class(hero).data)
