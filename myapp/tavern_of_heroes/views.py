from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Hero, Item


def index(request):
    hero_list = Hero.objects.order_by('creation_data')
    context = {'hero_list': hero_list}
    return render(request, 'tavern_of_heroes/index.html', context)


def hero_ditail(request, hero_id):
    hero = get_object_or_404(Hero, pk=hero_id)
    context = {'hero': hero}
    return render(request, 'tavern_of_heroes/hero_ditail.html', context)


def items_list(request):
    items = Item.objects.all()
    context = {'items_list': items}
    return render(request, 'tavern_of_heroes/items_list.html', context)


def item_ditail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {'item': item}
    return render(request, 'tavern_of_heroes/item_ditail.html', context)


def level_up(request, hero_id):
    hero = get_object_or_404(Hero, pk=hero_id)
    hero.level_up()
    context = {'hero': hero}
    return render(request, 'tavern_of_heroes/level_up.html', context)
