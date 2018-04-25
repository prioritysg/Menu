from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from item.views import items, item_details, item_add, item_uom_add

urlpatterns = [

    path('list/', items, name='items'),
    path('add/', item_add, name='add_item'),
    path('uom/add/', item_uom_add, name='add_uom_item'),
    path('<int:item_id>/details/', item_details, name='item_details'),

]
