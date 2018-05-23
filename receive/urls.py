from django.urls import path

from item.views import item_edit
from receive.views import orders, order_add, order_details, order_details_add, order_edit

urlpatterns = [

    path('list/', orders, name='orders'),
    path('add/', order_add, name='add_order'),
    path('details/add/', order_details_add, name='add_order_details'),
    # path('uom/<int:item_id>/edit/', item_uom_edit, name='edit_uom_item'),
    path('/<int:order_id>/edit/', order_edit, name='edit_order'),
    path('<int:order_id>/details/', order_details, name='order_details'),

]
