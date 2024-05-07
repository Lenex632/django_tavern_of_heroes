from ..models import Hero, Item
from rest_framework import generics, response
from .serializers import HeroSerializer, ItemSerializer


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
