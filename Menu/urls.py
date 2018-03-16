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
from django.urls import path
from django.contrib.auth import views as auth_views

from app.forms import UserLoginForm
from app.views import (index, receiving, item, settings as setting_view, SignUpView, home, shipping, mobile, reports, inventory
, organization_settings, client_settings, security_settings, remove_user)
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name='index'),
                  path('receiving', receiving, name='receiving'),
                  path('shipping', shipping, name='shipping'),
                  path('mobile', mobile, name='mobile'),
                  path('reports', reports, name='reports'),
                  path('inventory', inventory, name='inventory'),
                  path('home', home, name='home'),
                  path('organization_settings', organization_settings, name='organization_settings'),
                  path('security_settings', security_settings, name='security_settings'),
                  path('client_settings', client_settings, name='client_settings'),
                  path('item', item, name='item'),
                  path('settings', setting_view, name='settings'),
                  path('remove/user/', remove_user, name='remove_user'),
                  path(r'login/', auth_views.login,
                       {'template_name': 'login.html', 'authentication_form': UserLoginForm},
                       name='login'),
                  path(r'logout/', auth_views.logout, name='logout'),
                  path('signup/', SignUpView.as_view(), name='signup'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
