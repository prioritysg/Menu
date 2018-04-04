from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView

from app.forms import UserSignUpForm, GroupAccessForm, UserEditForm, UserAddForm, OrganizationForm, \
    OrganizationsClientChargeCodeForm, OrganizationsCarrierDetailForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from app.models import UserGroup, GroupAccess, Organization, OrganizationsClientChargeCode, OrganizationsCarrierDetail
from app.utils import add_user_regular_group


@login_required(login_url='/login/')
def client_settings(request):
    return render(request, 'settings_client.html', {'tab': 'client_settings'})


@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html', {'tab': 'home'})


def index(request):
    return render(request, 'index.html', {})


@login_required(login_url='/login/')
def inventory(request):
    return render(request, 'inventory.html', {'tab': 'inventory'})


@login_required(login_url='/login/')
def item(request):
    return render(request, 'item.html', {'tab': 'item'})


@login_required(login_url='/login/')
def mobile(request):
    return render(request, 'mobile.html', {'tab': 'mobile'})


@login_required(login_url='/login/')
def organization_add(request):
    form = OrganizationForm()
    if request.POST:
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('organization_settings'))

    request.session['next_tab'] = 'org'
    return render(request, 'settings_organization_add_edit.html',
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

    request.session['next_tab'] = 'org'
    return render(request, 'settings_organization_add_edit.html',
                  {'tab': 'organization_settings', 'form': form})


@login_required(login_url='/login/')
def organization_carrier_add(request):
    form = OrganizationsCarrierDetailForm()
    if request.POST:
        form = OrganizationsCarrierDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('organization_settings'))

    request.session['next_tab'] = 'carrier'
    return render(request, 'settings_organization_carrier_add_edit.html',
                  {'tab': 'organization_settings', 'form': form, 'add': True})


@login_required(login_url='/login/')
def organization_carrier_edit(request, organization_id):
    instance = OrganizationsCarrierDetail.objects.get(id=organization_id)

    if request.POST:
        form = OrganizationsCarrierDetailForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('organization_settings'))
    else:
        form = OrganizationsCarrierDetailForm(instance=instance)

    request.session['next_tab'] = 'carrier'
    return render(request, 'settings_organization_carrier_add_edit.html',
                  {'tab': 'organization_settings', 'form': form})


@login_required(login_url='/login/')
def organization_client_charge_add(request):
    form = OrganizationsClientChargeCodeForm()
    if request.POST:
        form = OrganizationsClientChargeCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('organization_settings'))

    request.session['next_tab'] = 'client'
    return render(request, 'settings_organization_client_add_edit.html',
                  {'tab': 'organization_settings', 'form': form, 'add': True})


@login_required(login_url='/login/')
def organization_client_charge_edit(request, organization_id):
    instance = OrganizationsClientChargeCode.objects.get(id=organization_id)
    if request.POST:
        form = OrganizationsClientChargeCodeForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('organization_settings'))
    else:
        form = OrganizationsClientChargeCodeForm(instance=instance)

    request.session['next_tab'] = 'client'
    return render(request, 'settings_organization_client_add_edit.html',
                  {'tab': 'organization_settings', 'form': form})


@login_required(login_url='/login/')
def organization_settings(request):
    next_tab = 'org'
    if 'next_tab' in request.session:
        next_tab = request.session.get('next_tab')
        del request.session['next_tab']
        request.session.modified = True

    organizations = Organization.objects.all().order_by('-id')
    organizations_charge = OrganizationsClientChargeCode.objects.all().order_by('-id')
    organizations_carrier = OrganizationsCarrierDetail.objects.all().order_by('-id')

    if request.POST and request.POST.get('search'):
        search = request.POST.get('search')
        organizations = Organization.objects.filter(org_id__icontains=search).order_by('-id')

    return render(request, 'settings_organization.html',
                  {'tab': 'organization_settings', 'organizations': organizations,
                   'organizations_charge': organizations_charge, 'next_tab': next_tab,
                   'organizations_carrier': organizations_carrier, 'search': request.POST.get('search', False)})


@login_required(login_url='/login/')
def receiving(request):
    return render(request, 'receiving.html', {'tab': 'receiving'})


@login_required(login_url='/login/')
def remove_user(request):
    if request.POST:
        user_id = request.POST.get('id')
        User.objects.filter(id=user_id).delete()
    return redirect(reverse('security_settings'))


@login_required(login_url='/login/')
def reports(request):
    return render(request, 'reports.html', {'tab': 'reports'})


@login_required(login_url='/login/')
def security_settings(request):
    next_tab = None
    if 'next_tab' in request.session:
        next_tab = request.session.get('next_tab')
        del request.session['next_tab']
        request.session.modified = True
    if request.POST:
        requested_data = request.POST.copy()
        updated_group = GroupAccess.objects.get(id=request.POST.get('id'))
        requested_data['user_group'] = updated_group.id
        updated_form = GroupAccessForm(requested_data, instance=updated_group)
        next_tab = 'group'
        if updated_form.is_valid():
            updated_form.save()

    users = User.objects.all().order_by('id')
    for user in users:
        setattr(user, 'form', UserEditForm(instance=user))

    groups = GroupAccess.objects.all().order_by('id')
    forms_array = [{'id': group.id, 'form': GroupAccessForm(instance=group)} for group in groups]
    user_form = UserEditForm()
    return render(request, 'settings_security.html',
                  {'tab': 'security_settings', 'users': users, 'groups': groups, 'form_array': forms_array,
                   'user_form': user_form, 'next_tab': next_tab})


@login_required(login_url='/login/')
def settings(request):
    return render(request, 'settings.html', {'tab': 'settings'})


@login_required(login_url='/login/')
def shipping(request):
    return render(request, 'shipping.html', {'tab': 'shipping'})


class SignUpView(FormView):
    form_class = UserSignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('index')
    extra_context = {'tab': 'signup'}

    def form_valid(self, form):
        new_user = form.save()
        add_user_regular_group(new_user)
        login(self.request, new_user)
        return super(SignUpView, self).form_valid(form)


def user_add(request):
    if request.POST:
        requested_data = request.POST.copy()
        create_user_form = UserAddForm(requested_data)
        if create_user_form.is_valid():
            user = create_user_form.save()
            group = UserGroup.objects.filter(user_type=requested_data.get('group')).first()
            if user not in group.users.all():
                group.users.add(user)
        else:
            return render(request, 'settings_security_user_adduser.html',
                          {'tab': 'security_settings', 'form': create_user_form})

        request.session['next_tab'] = 'user'
        return redirect(reverse('security_settings'))

    form = UserAddForm()
    return render(request, 'settings_security_user_adduser.html', {'tab': 'security_settings', 'form': form})


def user_edit(request):
    requested_data = request.POST.copy()
    user_to_edit = User.objects.get(id=request.POST.get('id'))
    updated_form = UserEditForm(requested_data, instance=user_to_edit)
    if updated_form.is_valid():
        user = updated_form.save()
        group = UserGroup.objects.filter(user_type=requested_data.get('group')).first()
        if user not in group.users.all():
            if user.usergroup_set.all():
                user.usergroup_set.all().first().users.remove(user)
            group.users.add(user)

    request.session['next_tab'] = 'user'
    return redirect(reverse('security_settings'))
