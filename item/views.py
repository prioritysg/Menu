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
    items = Item.objects.all().order_by('organization__org_id', 'item_code')
    if request.POST:
        if request.POST.get('org') and not request.POST.get('org') == '-1':
            selected_org = Organization.objects.filter(id=request.POST.get('org')).first()
            items = items.filter(organization_id=request.POST.get('org'))
        if request.POST.get('itemcode'):
            items = items.filter(item_code__icontains=request.POST.get('itemcode').lower())
    elif request.GET.get('org', -1) and int(request.GET.get('org', -1)) != -1:
        selected_org = Organization.objects.filter(id=request.GET.get('org')).first()
        items = items.filter(organization_id=request.GET.get('org'))

    return render(request, 'items.html',
                  {'tab': 'item', 'new_tab': 'item', 'clients': clients, 'items': items, 'selected_org': selected_org})


@login_required(login_url='/login/')
def item_add(request):
    form = ItemForm(org_id=request.GET.get('org_id', -1))
    if request.POST:
        form = ItemForm(request.POST, org_id=request.GET.get('org_id', -1))
        if form.is_valid():
            form.save()
            return redirect('%s?%s=%s' % (reverse('items'), 'org', request.GET.get('org_id', -1)))

    org = Organization.objects.filter(id=request.GET.get('org_id', -1)).first()
    return render(request, 'item_add.html', {'tab': 'item_details', 'form': form, 'client': org})


@login_required(login_url='/login/')
def item_uom_add(request):
    form = ItemUOMForm(item_id=request.GET.get('item_id', -1))
    if request.POST:
        form = ItemUOMForm(request.POST, item_id=request.GET.get('item_id', -1))
        if form.is_valid():
            item_uom = form.save()
            if request.POST.get('english'):
                item_uom.weight_metric = item_uom.weight_eng * 0.45
                item_uom.length_metric = item_uom.length_eng * 2.45
                item_uom.width_metric = item_uom.width_eng * 2.45
                item_uom.height_metric = item_uom.height_eng * 2.45
            elif request.POST.get('metric'):
                item_uom.weight_eng = item_uom.weight_metric / 0.45
                item_uom.length_eng = item_uom.length_metric / 2.45
                item_uom.width_eng = item_uom.width_metric / 2.45
                item_uom.height_eng = item_uom.height_metric / 2.45
            item_uom.save()
            return redirect(reverse('item_details', args=[item_uom.item.id]))

    item = Item.objects.filter(id=request.GET.get('item_id', -1)).first()
    return render(request, 'item_uom_add_edit.html', {'tab': 'item_details', 'form': form, 'item': item})


@login_required(login_url='/login/')
def item_edit(request, item_id):
    item = Item.objects.filter(id=item_id).first()
    form = ItemForm(instance=item, org_id=item.organization.id)
    if request.POST:
        form = ItemForm(request.POST, instance=item, org_id=item.organization.id)
        if form.is_valid():
            form.save()
            return redirect('%s?%s=%s' % (reverse('items'), 'org', item.organization.id))

    return render(request, 'item_add.html', {'tab': 'item_details', 'form': form, 'client': item.organization})


@login_required(login_url='/login/')
def item_uom_edit(request, item_id):
    item_uom = ItemUom.objects.filter(id=item_id).first()
    form = ItemUOMForm(instance=item_uom, item_id=item_uom.item.id)
    if request.POST:
        form = ItemUOMForm(request.POST, instance=item_uom, item_id=item_uom.item.id)
        if form.is_valid():
            item_uom = form.save()
            if request.POST.get('english'):
                item_uom.weight_metric = item_uom.weight_eng * 0.45
                item_uom.length_metric = item_uom.length_eng * 2.45
                item_uom.width_metric = item_uom.width_eng * 2.45
                item_uom.height_metric = item_uom.height_eng * 2.45
            elif request.POST.get('metric'):
                item_uom.weight_eng = item_uom.weight_metric / 0.45
                item_uom.length_eng = item_uom.length_metric / 2.45
                item_uom.width_eng = item_uom.width_metric / 2.45
                item_uom.height_eng = item_uom.height_metric / 2.45
            item_uom.save()
            return redirect(reverse('item_details', args=[item_uom.item.id]))

    item = Item.objects.filter(id=item_uom.item.id).first()
    return render(request, 'item_uom_add_edit.html', {'tab': 'item_details', 'form': form, 'item': item})


@login_required(login_url='/login/')
def item_details(request, item_id):
    item = Item.objects.filter(id=item_id).first()
    related_items = ItemUom.objects.filter(item=item).order_by('pack_type', 'pack')
    return render(request, 'item_details.html',
                  {'tab': 'item', 'new_tab': 'item_details', 'item': item, 'related_items': related_items})
