from django.shortcuts import render, redirect
from django.urls import reverse

from app.forms import (OrganizationForm, OrganizationsClientChargeCodeForm, OrganizationsCarrierDetailForm)
from django.contrib.auth.decorators import login_required

from app.models import Organization, OrganizationsClientChargeCode, OrganizationsCarrierDetail
from app.utils import perform_search


@login_required(login_url='/login/')
def organization_add(request):
    form = OrganizationForm()
    if request.POST:
        form = OrganizationForm(request.POST)
        if form.is_valid():
            new_organization = form.save()
            if new_organization.category == Organization.CLIENT:
                return redirect(reverse('organization_client'))
            elif new_organization.category == Organization.CARRIER:
                return redirect(reverse('organization_carrier'))

            return redirect(reverse('organization_customer'))

    return render(request, 'organization/settings_organization_add_edit.html',
                  {'tab': 'organization_settings', 'form': form, 'add': True})


@login_required(login_url='/login/')
def organization_edit(request, organization_id):
    instance = Organization.objects.get(id=organization_id)

    if request.POST:
        form = OrganizationForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('organization_settings'))
    else:
        form = OrganizationForm(instance=instance)

    return render(request, 'organization/settings_organization_add_edit.html',
                  {'tab': 'organization_settings', 'form': form})


@login_required(login_url='/login/')
def organization_carrier_add(request):
    form = OrganizationsCarrierDetailForm()
    if request.POST:
        form = OrganizationsCarrierDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('organization_carrier_details'))

    return render(request, 'organization/settings_organization_carrier_add_edit.html',
                  {'tab': 'organization_settings', 'form': form, 'add': True})


@login_required(login_url='/login/')
def organization_carrier_edit(request, organization_id):
    instance = OrganizationsCarrierDetail.objects.get(id=organization_id)

    if request.POST:
        form = OrganizationsCarrierDetailForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('organization_carrier_details'))
    else:
        form = OrganizationsCarrierDetailForm(instance=instance)

    return render(request, 'organization/settings_organization_carrier_add_edit.html',
                  {'tab': 'organization_settings', 'form': form})


@login_required(login_url='/login/')
def organization_client_charge_add(request):
    form = OrganizationsClientChargeCodeForm()
    if request.POST:
        form = OrganizationsClientChargeCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('organization_client_invoices'))

    return render(request, 'organization/settings_organization_client_add_edit.html',
                  {'tab': 'organization_settings', 'form': form, 'add': True})


@login_required(login_url='/login/')
def organization_client_charge_edit(request, organization_id):
    instance = OrganizationsClientChargeCode.objects.get(id=organization_id)
    if request.POST:
        form = OrganizationsClientChargeCodeForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('organization_client_invoices'))
    else:
        form = OrganizationsClientChargeCodeForm(instance=instance)

    return render(request, 'organization/settings_organization_client_add_edit.html',
                  {'tab': 'organization_settings', 'form': form})


@login_required(login_url='/login/')
def organization_settings(request):
    organizations = Organization.objects.all().order_by('-id')
    organizations_charge = OrganizationsClientChargeCode.objects.all().order_by('-id')
    organizations_carrier = OrganizationsCarrierDetail.objects.all().order_by('-id')

    organizations = perform_search(organizations, request)

    return render(request, 'organization/settings_organization.html',
                  {'tab': 'organization_settings', 'organizations': organizations,
                   'organizations_charge': organizations_charge,
                   'organizations_carrier': organizations_carrier, 'search': request.POST.get('search', False)})


@login_required(login_url='/login/')
def organization_client(request):
    organizations = Organization.objects.all().order_by('-id')
    organizations = perform_search(organizations, request)

    return render(request, 'organization/organization_client.html',
                  {'tab': 'org_client', 'organizations': organizations, 'search': request.POST.get('search', False)})


@login_required(login_url='/login/')
def organization_client_invoices(request):
    org_id = request.GET.get('org_id', 0) or 0
    organizations_charge = OrganizationsClientChargeCode.objects.all().order_by('-id')

    if org_id:
        organizations_charge = organizations_charge.filter(organization_id=org_id)

    return render(request, 'organization/organization_client_invoice.html',
                  {'tab': 'org_client', 'organizations_charge': organizations_charge,
                   'search': request.POST.get('search', False)})


@login_required(login_url='/login/')
def organization_customer(request):
    organizations = Organization.objects.all().order_by('-id')
    organizations = perform_search(organizations, request)

    return render(request, 'organization/organization_customer.html',
                  {'tab': 'org_customer', 'organizations': organizations, 'search': request.POST.get('search', False)})


@login_required(login_url='/login/')
def organization_carrier(request):
    organizations = Organization.objects.all().order_by('-id')
    organizations = perform_search(organizations, request)

    return render(request, 'organization/organization_carrier.html',
                  {'tab': 'org_carrier', 'organizations': organizations, 'search': request.POST.get('search', False)})


@login_required(login_url='/login/')
def organization_carrier_details(request):
    org_id = request.GET.get('org_id', 0) or 0
    organizations_carrier = OrganizationsCarrierDetail.objects.all().order_by('-id')

    if org_id:
        organizations_carrier = organizations_carrier.filter(organization_id=org_id)

    return render(request, 'organization/organization_carrier_details.html',
                  {'tab': 'org_carrier', 'organizations_carrier': organizations_carrier,
                   'search': request.POST.get('search', False)})
