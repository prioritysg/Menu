from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from app.models import Organization
from item.forms import ItemForm, ItemUOMForm
from item.models import Item, ItemUom


@login_required(login_url='/login/')
def items(request):
    clients = Organization.objects.filter(category=Organization.CLIENT)
    selected_org = None
    items = Item.objects.all()
    if request.POST:
        if request.POST.get('org') and not request.POST.get('org') == '-1':
            selected_org = Organization.objects.filter(id=request.POST.get('org')).first()
            items = items.filter(organization_id=request.POST.get('org'))
        if request.POST.get('itemcode'):
            items = items.filter(item_code__icontains=request.POST.get('itemcode').lower())

    return render(request, 'items.html',
                  {'tab': 'item', 'new_tab': 'item', 'clients': clients, 'items': items, 'selected_org': selected_org})


@login_required(login_url='/login/')
def item_add(request):
    form = ItemForm(org_id=request.GET.get('org_id', -1))
    if request.POST:
        form = ItemForm(request.POST, org_id=request.GET.get('org_id', -1))
        if form.is_valid():
            form.save()
            return redirect(reverse('items'))

    return render(request, 'item_add.html', {'tab': 'item_details', 'form': form})


@login_required(login_url='/login/')
def item_uom_add(request):
    form = ItemUOMForm(item_id=request.GET.get('item_id', -1))
    if request.POST:
        form = ItemUOMForm(request.POST, item_id=request.GET.get('item_id', -1))
        if form.is_valid():
            item_uom = form.save()
            return redirect(reverse('item_details', args=[item_uom.item.id]))

    return render(request, 'item_add.html', {'tab': 'item_details', 'form': form})


@login_required(login_url='/login/')
def item_details(request, item_id):
    item = Item.objects.filter(id=item_id).first()
    related_items = ItemUom.objects.filter(item=item)
    return render(request, 'item_details.html',
                  {'tab': 'item', 'new_tab': 'item_details', 'item': item, 'related_items': related_items})
