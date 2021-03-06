from django.contrib.auth.models import User
from django.core.files import File
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView

from app.forms import UserSignUpForm, GroupAccessForm, UserEditForm, UserAddForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from app.decorators import permission_required_for_item

from app.models import UserGroup, GroupAccess
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
@permission_required_for_item('inventory', raise_exception=True)
def inventory(request):
    return render(request, 'inventory.html', {'tab': 'inventory'})


# @login_required(login_url='/login/')
# def item(request):
#     return render(request, 'item.html', {'tab': 'item'})


@login_required(login_url='/login/')
@permission_required_for_item('mobile', raise_exception=True)
def mobile(request):
    return render(request, 'mobile.html', {'tab': 'mobile'})


@login_required(login_url='/login/')
@permission_required_for_item('receiving', raise_exception=True)
def receiving(request):
    return render(request, 'receiving.html', {'tab': 'receiving'})


@login_required(login_url='/login/')
def remove_user(request):
    if request.POST:
        user_id = request.POST.get('id')
        User.objects.filter(id=user_id).delete()
        request.session['next_tab'] = 'user'
    return redirect(reverse('security_settings'))


@login_required(login_url='/login/')
@permission_required_for_item('reports', raise_exception=True)
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

    users = User.objects.all().order_by('username')
    for user in users:
        setattr(user, 'form', UserEditForm(instance=user))

    groups = GroupAccess.objects.all().order_by('id')
    forms_array = [{'id': group.id, 'form': GroupAccessForm(
        instance=group)} for group in groups]
    user_form = UserEditForm()
    return render(request, 'settings_security.html',
                  {'tab': 'security_settings', 'users': users, 'groups': groups, 'form_array': forms_array,
                   'user_form': user_form, 'next_tab': next_tab})


@login_required(login_url='/login/')
@permission_required_for_item('settings', raise_exception=True)
def settings(request):
    return render(request, 'settings.html', {'tab': 'settings'})


@login_required(login_url='/login/')
@permission_required_for_item('shipping', raise_exception=True)
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
    form = UserAddForm()
    if request.POST:
        requested_data = request.POST.copy()
        create_user_form = UserAddForm(requested_data)
        if create_user_form.is_valid():
            user = create_user_form.save()
            group = UserGroup.objects.filter(
                user_type=requested_data.get('group')).first()
            if user not in group.users.all():
                group.users.add(user)
        else:
            return render(request, 'settings_security_user_adduser.html',
                          {'tab': 'security_settings', 'form': create_user_form})

        request.session['next_tab'] = 'user'
        return redirect(reverse('security_settings'))

    return render(request, 'settings_security_user_adduser.html', {'tab': 'security_settings', 'form': form})


def user_edit(request):
    requested_data = request.POST.copy()
    user_to_edit = User.objects.get(id=request.POST.get('id'))
    updated_form = UserEditForm(requested_data, instance=user_to_edit)
    if updated_form.is_valid():
        user = updated_form.save()
        group = UserGroup.objects.filter(
            user_type=requested_data.get('group')).first()
        if user not in group.users.all():
            if user.usergroup_set.all():
                user.usergroup_set.all().first().users.remove(user)
            group.users.add(user)

    request.session['next_tab'] = 'user'
    return redirect(reverse('security_settings'))
