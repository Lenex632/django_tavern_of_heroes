from django.shortcuts import render, get_object_or_404, reverse, redirect

from .models import Item


def items_list(request):
    items = Item.objects.all()
    context = {'items_list': items, 'item_types': Item.ItemTypes.choices}
    return render(request, 'tavern_of_heroes/items/items_list.html', context)


def item_ditail(request, item_id: int):
    item = get_object_or_404(Item, pk=item_id)
    context = {'item': item}
    return render(request, 'tavern_of_heroes/items/item_ditail.html', context)


def create_item(request):
    new_item = Item()
    new_item.name = request.POST['choose_item_name']
    new_item.type = request.POST['choose_item_type']
    new_item.description = request.POST['choose_item_description']
    new_item.save()
    context = {'item': new_item}
    return render(request, 'tavern_of_heroes/items/create_item.html', context)


def delete_item(request, item_id: int):
    item = get_object_or_404(Item, pk=item_id)
    # message = f'Предмет {item.name} был выброшен со склада'
    item.delete()
    return redirect('items_list')
