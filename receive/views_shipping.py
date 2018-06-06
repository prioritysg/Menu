from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from app.models import Organization
from item.forms import ItemForm, ItemUOMForm
from item.models import Item, ItemUom
from receive.forms import OrderForm, OrderDetailForm, ShippingOrderForm
from receive.models import Order, OrderDetail


@login_required(login_url='/login/')
def orders(request):
    clients = Organization.objects.filter(category=Organization.CLIENT)
    selected_org = None
    orders = Order.objects.filter(order_type=Order.SHIPPING)
    search = ''
    if request.POST:
        if request.POST.get('org') and not request.POST.get('org') == '-1':
            selected_org = Organization.objects.filter(id=request.POST.get('org')).first()
            orders = orders.filter(organization_id=request.POST.get('org'))
        if request.POST.get('order'):
            orders = orders.filter(order_no__icontains=request.POST.get('order').lower())
            search = request.POST.get('order')

    elif request.GET.get('org', -1) and int(request.GET.get('org', -1)) != -1:
        selected_org = Organization.objects.filter(id=request.GET.get('org')).first()
        orders = orders.filter(organization_id=request.GET.get('org'))
        search = request.POST.get('order', None)

    return render(request, 'shipping/orders.html',
                  {'tab': 'shipping', 'new_tab': 'orders', 'orders': orders, 'clients': clients,
                   'selected_org': selected_org, 'search': search})


@login_required(login_url='/login/')
def order_add(request):
    org_id = request.GET.get('org_id', -1)
    selected_org = Organization.objects.filter(id=org_id).first()
    form = ShippingOrderForm(order_id=org_id)
    if request.POST:
        form = ShippingOrderForm(request.POST, order_id=org_id)
        if form.is_valid():
            order = form.save()
            order.order_type = Order.SHIPPING
            order.save()
            return redirect('%s?%s=%s' % (reverse('shipping_orders'), 'org', order.organization.id))
    return render(request, 'shipping/order_add_edit.html',
                  {'tab': 'shipping', 'form': form, 'selected_org': selected_org})


@login_required(login_url='/login/')
def order_edit(request, order_id):
    order = Order.objects.filter(id=order_id).first()
    form = ShippingOrderForm(instance=order, order_id=order.id)
    if request.POST:
        form = ShippingOrderForm(request.POST, instance=order, order_id=order.id)
        if form.is_valid():
            form.save()
            return redirect('%s?%s=%s' % (reverse('shipping_orders'), 'org', order.organization.id))

    return render(request, 'shipping/order_add_edit.html',
                  {'tab': 'shipping', 'form': form, 'selected_org': order.organization})


@login_required(login_url='/login/')
def order_details(request, order_id):
    order = Order.objects.filter(id=order_id).first()
    related_orders = OrderDetail.objects.filter(order_id=order_id)
    return render(request, 'shipping/order_details.html',
                  {'tab': 'shipping', 'new_tab': 'order_details',
                   'selected_order': order,
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
            return redirect(reverse('shipping_order_details', args=[order_detail.order.id]))

    return render(request, 'shipping/order_details_add_edit.html', {'tab': 'shipping', 'form': form, 'order': order})


@login_required(login_url='/login/')
def order_details_edit(request, details_id):
    order_id = request.GET.get('order_id', -1)
    order_detail = OrderDetail.objects.filter(id=details_id).first()
    form = OrderDetailForm(instance=order_detail, order_id=order_id)
    order = None
    if order_detail:
        order = order_detail.order

    if request.POST:
        form = OrderDetailForm(request.POST, instance=order_detail, order_id=order_id)
        if form.is_valid():
            order_detail = form.save()
            return redirect(reverse('shipping_order_details', args=[order_detail.order.id]))

    return render(request, 'shipping/order_details_add_edit.html', {'tab': 'shipping', 'form': form, 'order': order})


def delete_order_detail(request, detail_id):
    order_detail = OrderDetail.objects.filter(id=detail_id)
    if order_detail:
        order = order_detail[0].order
        order_detail.delete()

    return redirect(reverse('shipping_order_details', args=[order.id]))


def load_items_uom(request):
    item = request.GET.get('item')
    items = ItemUom.objects.filter(item_id=item)
    return render(request, 'shipping/item_uom_dropdown.html', {'item_uoms': items})
