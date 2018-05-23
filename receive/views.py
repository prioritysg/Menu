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

    elif request.GET.get('org', -1) and int(request.GET.get('org', -1)) != -1:
        selected_org = Organization.objects.filter(id=request.GET.get('org')).first()
        orders = orders.filter(organization_id=request.GET.get('org'))
        search = request.POST.get('order', None)

    return render(request, 'orders.html',
                  {'tab': 'receiving', 'new_tab': 'orders', 'orders': orders, 'clients': clients,
                   'selected_org': selected_org, 'search': search})


@login_required(login_url='/login/')
def order_add(request):
    org_id = request.GET.get('org_id', -1)
    selected_org = Organization.objects.filter(id=org_id).first()
    form = OrderForm(order_id=org_id)
    if request.POST:
        form = OrderForm(request.POST, order_id=org_id)
        if form.is_valid():
            form.save()
            return redirect(reverse('orders'))
    return render(request, 'order_add_edit.html', {'tab': 'receiving', 'form': form, 'selected_org': selected_org})


@login_required(login_url='/login/')
def order_edit(request, order_id):
    order = Order.objects.filter(id=order_id).first()
    form = OrderForm(instance=order, order_id=order.id)
    if request.POST:
        form = OrderForm(request.POST, instance=order, order_id=order.id)
        if form.is_valid():
            form.save()
            return redirect('%s?%s=%s' % (reverse('orders'), 'org', order.organization.id))

    return render(request, 'order_add_edit.html',
                  {'tab': 'receiving', 'form': form, 'selected_org': order.organization})


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
            return redirect(reverse('order_details', args=[order_detail.order.id]))

    return render(request, 'order_details_add_edit.html', {'tab': 'receiving', 'form': form, 'order': order})
