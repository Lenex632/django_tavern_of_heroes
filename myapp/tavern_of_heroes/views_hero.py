from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Hero, Item


def tavern(request) -> HttpResponse:
    user = request.user
    hero_list = []
    if user.is_superuser:
        hero_list = Hero.objects.order_by('creation_data')
    elif user.is_authenticated:
        hero_list = Hero.objects.order_by('creation_data').filter(user=user)
    context = {'user': user, 'hero_list': hero_list, 'classes': Hero.CLASSES}

    return render(request, 'tavern_of_heroes/heroes/tavern.html', context)


def hero_ditail(request, hero_id: int) -> HttpResponse:
    hero = get_object_or_404(Hero, pk=hero_id)
    context = {'hero': hero}

    return render(request, 'tavern_of_heroes/heroes/hero_ditail.html', context)


@login_required
def level_up(request, hero_id: int) -> HttpResponse:
    user = request.user
    hero = get_object_or_404(Hero, pk=hero_id)
    if user == hero.user or user.is_superuser:
        hero.level_up()
        messages.success(request, f'{hero.name} теперь {hero.level} уровня!')
    else:
        messages.error(request, 'Это не ваш герой!')
        return redirect('app:hero_ditail', hero_id)

    return redirect('app:hero_ditail', hero_id)


@login_required
def create_hero(request) -> HttpResponse:
    new_hero = Hero()
    new_hero.user = request.user
    new_hero.name = request.POST['choose_hero_name']
    new_hero.hero_class = request.POST['choose_hero_class']
    new_hero.description = request.POST['choose_hero_description']
    new_hero.save()
    messages.success(request, f'Вы создали нового героя {new_hero.name}')

    return redirect('app:tavern')


@login_required
def delete_hero(request, hero_id: int) -> HttpResponseRedirect:
    user = request.user
    hero = get_object_or_404(Hero, pk=hero_id)
    if user == hero.user or user.is_superuser:
        messages.success(request, f'Герой {hero.name} уже напился и пошёл спать')
        hero.delete()
    else:
        messages.error(request, 'Это не ваш герой!')
        return redirect('app:hero_ditail', hero_id)

    return redirect('app:tavern')


def hero_item_detail(request, hero_id: int, item_id: int) -> HttpResponse:
    hero = get_object_or_404(Hero, pk=hero_id)
    item = Item.objects.get(pk=item_id)
    context = {'hero': hero, 'item': item}

    return render(request, 'tavern_of_heroes/heroes/hero_item_detail.html', context)


@login_required
def remove_item_from_inventory(request, hero_id: int, item_id: int) -> HttpResponseRedirect:
    user = request.user
    hero = get_object_or_404(Hero, pk=hero_id)
    item = Item.objects.get(pk=item_id)
    if user == hero.user or user.is_superuser:
        messages.success(request, f'Герой {hero.name} где-то потерял предмет {item.name}.')
        hero.remove_item_from_inventory(item)
    else:
        messages.error(request, 'Это не ваш герой!')
        return redirect('app:hero_ditail', hero_id)

    return redirect('app:hero_ditail', hero_id=hero_id)
