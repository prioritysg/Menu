from django.urls import path
from receive.views import orders, order_add, order_details, order_details_add, order_edit, order_details_edit, \
    delete_order_detail, load_items_uom

urlpatterns = [

    path('list/', orders, name='orders'),
    path('add/', order_add, name='add_order'),
    path('load/items/', load_items_uom, name='load_item_uom'),
    path('details/add/', order_details_add, name='add_order_details'),
    path('detail/<int:details_id>/edit/', order_details_edit, name='edit_detail'),
    path('detail/<int:detail_id>/delete/', delete_order_detail, name='delete_detail'),
    path('/<int:order_id>/edit/', order_edit, name='edit_order'),
    path('<int:order_id>/details/', order_details, name='order_details'),

]
