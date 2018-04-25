from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from app.models import Organization
from item.forms import ItemForm, ItemUOMForm
from item.models import Item, ItemUom


@login_required(login_url='/login/')
def items(request):
    clients = Organization.objects.filter(category=Organization.CLIENT)
    items = Item.objects.all()
    return render(request, 'items.html', {'tab': 'item', 'new_tab': 'item', 'clients': clients, 'items': items})


@login_required(login_url='/login/')
def item_add(request):
    form = ItemForm()
    if request.POST:
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('items'))

    return render(request, 'item_add.html', {'tab': 'item_details', 'form': form})


@login_required(login_url='/login/')
def item_uom_add(request):
    form = ItemUOMForm()
    if request.POST:
        form = ItemUOMForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('items'))

    return render(request, 'item_add.html', {'tab': 'item_details', 'form': form})


@login_required(login_url='/login/')
def item_details(request, item_id):
    item = Item.objects.filter(id=item_id).first()
    related_items = ItemUom.objects.filter(item=item)
    return render(request, 'item_details.html',
                  {'tab': 'item', 'new_tab': 'item_details', 'item': item, 'related_items': related_items})
