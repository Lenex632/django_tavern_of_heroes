from django.shortcuts import render, get_object_or_404, redirect

from .models import Hero


def tavern(request):
    hero_list = Hero.objects.order_by('creation_data')
    context = {'hero_list': hero_list, 'classes': Hero.CLASSES}
    return render(request, 'tavern_of_heroes/heroes/index.html', context)


def hero_ditail(request, hero_id):
    hero = get_object_or_404(Hero, pk=hero_id)
    context = {'hero': hero}
    return render(request, 'tavern_of_heroes/heroes/hero_ditail.html', context)


def level_up(request, hero_id):
    hero = get_object_or_404(Hero, pk=hero_id)
    hero.level_up()
    context = {'hero': hero}
    return render(request, 'tavern_of_heroes/heroes/level_up.html', context)


def create_hero(request):
    new_hero = Hero()
    new_hero.name = request.POST['choose_hero_name']
    new_hero.hero_class = request.POST['choose_hero_class']
    new_hero.description = request.POST['choose_hero_description']
    new_hero.save()
    context = {'hero': new_hero}
    return render(request, 'tavern_of_heroes/heroes/create_hero.html', context)


def delete_hero(request, hero_id: int):
    hero = get_object_or_404(Hero, pk=hero_id)
    # message = f'Герой {item.name} уже напился и пошёл спать'
    hero.delete()
    return redirect('tavern')
