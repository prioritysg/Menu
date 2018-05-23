from django.urls import path, include

from item.views import items, item_details, item_add, item_uom_add, item_uom_edit, item_edit

urlpatterns = [

    path('list/', items, name='orders'),
    path('add/', item_add, name='add_order'),
    # path('uom/add/', item_uom_add, name='add_uom_item'),
    # path('uom/<int:item_id>/edit/', item_uom_edit, name='edit_uom_item'),
    # path('/<int:item_id>/edit/', item_edit, name='edit_item'),
    # path('<int:item_id>/details/', item_details, name='item_details'),

]
