from ..models import Item, Hero
from rest_framework import mixins, generics

from .serializers import HeroSerializer, ItemSerializer


class HeroesListView(generics.ListAPIView):
    queryset = Hero.objects.all().order_by('creation_data')
    serializer_class = HeroSerializer


class HeroDetailView(generics.RetrieveAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


class ItemsListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemsDetailView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CreateHeroView(generics.CreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
