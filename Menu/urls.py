"""Menu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from app.forms import UserLoginForm
from app.organization_views import organization_customer, organization_carrier, organization_carrier_details, \
    organization_client, organization_client_invoices, organization_settings, organization_add, organization_edit, \
    organization_client_charge_add, organization_client_charge_edit, organization_carrier_add, organization_carrier_edit
from app.views import (index, receiving, settings as setting_view, SignUpView, home, shipping, mobile, reports,
                       inventory, client_settings, security_settings, remove_user, user_edit, user_add)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name='index'),
                  path('receiving', receiving, name='receiving'),
                  path('shipping', shipping, name='shipping'),
                  path('mobile', mobile, name='mobile'),
                  path('reports', reports, name='reports'),
                  path('inventory', inventory, name='inventory'),
                  path('home', home, name='home'),

                  path('organization_customer', organization_customer, name='organization_customer'),
                  path('organization_carrier', organization_carrier, name='organization_carrier'),
                  path('organization_carrier_details', organization_carrier_details,
                       name='organization_carrier_details'),
                  path('organization_client', organization_client, name='organization_client'),
                  path('organization_client_invoices', organization_client_invoices,
                       name='organization_client_invoices'),

                  path('organization_settings', organization_settings, name='organization_settings'),
                  path('organization/add', organization_add, name='organization_add'),
                  path('organization/<int:organization_id>/edit', organization_edit, name='organization_edit'),

                  path('organization/charge/add', organization_client_charge_add, name='organization_charge_add'),
                  path('organization/charge/<int:organization_id>/edit', organization_client_charge_edit,
                       name='organization_charge_edit'),

                  path('organization/carrier/add', organization_carrier_add, name='organization_carrier_add'),
                  path('organization/carrier/<int:organization_id>/edit', organization_carrier_edit,
                       name='organization_carrier_edit'),

                  path('security_settings', security_settings, name='security_settings'),
                  path('client_settings', client_settings, name='client_settings'),

                  path('settings', setting_view, name='settings'),
                  path('remove/user/', remove_user, name='remove_user'),
                  path('edit/user/', user_edit, name='edit_user'),
                  path('add/user/', user_add, name='add_user'),
                  path(r'login/', auth_views.login,
                       {'template_name': 'login.html', 'authentication_form': UserLoginForm},
                       name='login'),
                  path(r'logout/', auth_views.logout, name='logout'),
                  path('signup/', SignUpView.as_view(), name='signup'),
                  path('item/', include('item.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
