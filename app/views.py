from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from app.forms import UserSignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from app.models import UserGroup, GroupAccess
from app.utils import add_user_regular_group


def index(request):
    return render(request, 'index.html', {})


@login_required(login_url='/login/')
def receiving(request):
    return render(request, 'receiving.html', {'tab': 'receiving'})


@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html', {'tab': 'home'})


@login_required(login_url='/login/')
def shipping(request):
    return render(request, 'shipping.html', {'tab': 'shipping'})


@login_required(login_url='/login/')
def inventory(request):
    return render(request, 'inventory.html', {'tab': 'inventory'})


@login_required(login_url='/login/')
def organization_settings(request):
    return render(request, 'organization_settings.html', {'tab': 'organization_settings'})


@login_required(login_url='/login/')
def security_settings(request):
    users = User.objects.all()
    groups = GroupAccess.objects.all()
    return render(request, 'security_settings.html', {'tab': 'security_settings', 'users': users, 'groups': groups})


@login_required(login_url='/login/')
def client_settings(request):
    return render(request, 'client_settings.html', {'tab': 'client_settings'})


@login_required(login_url='/login/')
def mobile(request):
    return render(request, 'mobile.html', {'tab': 'mobile'})


@login_required(login_url='/login/')
def reports(request):
    return render(request, 'reports.html', {'tab': 'reports'})


@login_required(login_url='/login/')
def item(request):
    return render(request, 'item.html', {'tab': 'item'})


@login_required(login_url='/login/')
def settings(request):
    return render(request, 'settings.html', {'tab': 'settings'})


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
