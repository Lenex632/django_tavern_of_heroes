from ..models import Hero, Item
from rest_framework import generics, response
from .serializers import HeroSerializer, ItemSerializer


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
