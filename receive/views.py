from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from app.models import Organization
from item.forms import ItemForm, ItemUOMForm
from item.models import Item, ItemUom
from receive.forms import OrderForm, OrderDetailForm
from receive.models import Order, OrderDetail


@login_required(login_url='/login/')
def orders(request):
    clients = Organization.objects.filter(category=Organization.CLIENT)
    selected_org = None
    orders = Order.objects.all()
    search = ''
    if request.POST:
        if request.POST.get('org') and not request.POST.get('org') == '-1':
            selected_org = Organization.objects.filter(id=request.POST.get('org')).first()
            orders = orders.filter(organization_id=request.POST.get('org'))
        if request.POST.get('order'):
            orders = orders.filter(order_no__icontains=request.POST.get('order').lower())
            search = request.POST.get('order')

    return render(request, 'orders.html',
                  {'tab': 'receiving', 'new_tab': 'orders', 'orders': orders, 'clients': clients,
                   'selected_org': selected_org, 'search': search})


@login_required(login_url='/login/')
def order_add(request):
    form = OrderForm()
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('orders'))
    return render(request, 'order_add_edit.html', {'tab': 'receiving', 'form': form})


# @login_required(login_url='/login/')
# def item_edit(request, item_id):
#     item = Item.objects.filter(id=item_id).first()
#     form = ItemForm(instance=item, org_id=item.organization.id)
#     if request.POST:
#         form = ItemForm(request.POST, instance=item, org_id=item.organization.id)
#         if form.is_valid():
#             form.save()
#             return redirect('%s?%s=%s' % (reverse('items'), 'org', item.organization.id))
#
#     return render(request, 'item_add.html', {'tab': 'item_details', 'form': form, 'client': item.organization})


# @login_required(login_url='/login/')
# def item_uom_edit(request, item_id):
#     item_uom = ItemUom.objects.filter(id=item_id).first()
#     form = ItemUOMForm(instance=item_uom, item_id=item_uom.item.id)
#     if request.POST:
#         form = ItemUOMForm(request.POST, instance=item_uom, item_id=item_uom.item.id)
#         if form.is_valid():
#             item_uom = form.save()
#             if request.POST.get('english'):
#                 item_uom.weight_metric = item_uom.weight_eng * 0.45
#                 item_uom.length_metric = item_uom.length_eng * 2.45
#                 item_uom.width_metric = item_uom.width_eng * 2.45
#                 item_uom.height_metric = item_uom.height_eng * 2.45
#             elif request.POST.get('metric'):
#                 item_uom.weight_eng = item_uom.weight_metric / 0.45
#                 item_uom.length_eng = item_uom.length_metric / 2.45
#                 item_uom.width_eng = item_uom.width_metric / 2.45
#                 item_uom.height_eng = item_uom.height_metric / 2.45
#             item_uom.save()
#             return redirect(reverse('item_details', args=[item_uom.item.id]))
#
#     item = Item.objects.filter(id=item_uom.item.id).first()
#     return render(request, 'item_uom_add_edit.html', {'tab': 'item_details', 'form': form, 'item': item})
#


@login_required(login_url='/login/')
def order_details(request, order_id):
    related_orders = OrderDetail.objects.filter(order_id=order_id)
    return render(request, 'order_details.html',
                  {'tab': 'receiving', 'new_tab': 'order_details',
                   'selected_order': related_orders[0].order if related_orders else '',
                   'related_orders': related_orders})


@login_required(login_url='/login/')
def order_details_add(request):
    order_id = request.GET.get('order_id', -1)
    form = OrderDetailForm(order_id=order_id)
    order = Order.objects.filter(id=order_id).first()
    if request.POST:
        form = OrderDetailForm(request.POST, order_id=order_id)
        if form.is_valid():
            order_detail = form.save()
            return redirect(reverse('order_details', args=[order_detail.order.id]))

    return render(request, 'order_details_add_edit.html', {'tab': 'receiving', 'form': form, 'order': order})
