from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from item.views import items, item_details

urlpatterns = [

    path('list/', items, name='items'),
    path('details/', item_details, name='item_details'),

]
