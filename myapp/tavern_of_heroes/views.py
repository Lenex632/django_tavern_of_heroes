from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Hero, Inventory


def index(request):
    hero_list = Hero.objects.order_by('creation_data')
    context = {'hero_list': hero_list}
    return render(request, 'tavern_of_heroes/index.html', context)


def description(request, hero_id):
    hero = get_object_or_404(Hero, pk=hero_id)
    inventory = Inventory.objects.get(hero=hero_id)
    context = {'hero': hero, 'inventory': inventory}
    return render(request, 'tavern_of_heroes/description.html', context)


def hero_class(request, hero_id):
    response = f"Класс героя {hero_id}."
    return HttpResponse(response)


def level_up(request, hero_id):
    return HttpResponse(f"Ты повысил уровень героя {hero_id}.")
