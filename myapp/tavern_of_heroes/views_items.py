from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Item, Hero


def items_list(request) -> HttpResponse:
    items = Item.objects.all()
    context = {'items_list': items, 'item_types': Item.ItemTypes.choices}
    return render(request, 'tavern_of_heroes/items/items_list.html', context)


def item_ditail(request, item_id: int) -> HttpResponse:
    item = get_object_or_404(Item, pk=item_id)
    heroes = Hero.objects.all()
    context = {'item': item, 'heroes': heroes}
    return render(request, 'tavern_of_heroes/items/item_ditail.html', context)


@login_required
def create_item(request) -> HttpResponse:
    user = request.user
    if user.is_superuser:
        new_item = Item()
        new_item.name = request.POST['choose_item_name']
        new_item.type = request.POST['choose_item_type']
        new_item.description = request.POST['choose_item_description']
        new_item.save()
        messages.success(request, f'{new_item.name} теперь доступен на складе таверны')
    else:
        messages.error(request, 'Жуликам тут не рады')
        return redirect('app:items_list')
    return redirect('app:items_list')


@login_required
def delete_item(request, item_id: int) -> HttpResponseRedirect:
    user = request.user
    if user.is_superuser:
        item = get_object_or_404(Item, pk=item_id)
        messages.success(request, f'Предмет {item.name} был выброшен со склада')
        item.delete()
    else:
        messages.error(request, 'Жуликам тут не рады')
        return redirect('app:item_ditail', item_id)
    return redirect('app:items_list')


@login_required
def give_item_to_hero(request, item_id: int) -> HttpResponseRedirect:
    user = request.user
    if user.is_superuser:
        item = get_object_or_404(Item, pk=item_id)
        hero_id = request.POST['choose_hero']
        hero = get_object_or_404(Hero, pk=hero_id)
        hero.give_item_to_hero(item)
        messages.success(request, f'Предмет {item.name} был передан герою {hero.name}')
    else:
        messages.error(request, 'Жуликам тут не рады')
        return redirect('app:item_ditail', item_id)
    return redirect('app:item_ditail', item_id)
