from django.urls import path
from receive.views import orders, order_add, order_details, order_details_add, order_edit, order_details_edit, \
    delete_order_detail, load_items_uom
import receive.views_shipping as shipping_views

urlpatterns = [

    path('list/', orders, name='orders'),
    path('add/', order_add, name='add_order'),
    path('load/items/', load_items_uom, name='load_item_uom'),
    path('details/add/', order_details_add, name='add_order_details'),
    path('detail/<int:details_id>/edit/', order_details_edit, name='edit_detail'),
    path('detail/<int:detail_id>/delete/', delete_order_detail, name='delete_detail'),
    path('<int:order_id>/edit/', order_edit, name='edit_order'),
    path('<int:order_id>/details/', order_details, name='order_details'),

    path('shipping/list/', shipping_views.orders, name='shipping_orders'),
    path('shipping/add/', shipping_views.order_add, name='shipping_add_order'),
    path('shipping/load/items/', shipping_views.load_items_uom, name='shipping_load_item_uom'),
    path('shipping/details/add/', shipping_views.order_details_add, name='shipping_add_order_details'),
    path('shipping/detail/<int:details_id>/edit/', shipping_views.order_details_edit, name='shipping_edit_detail'),
    path('shipping/detail/<int:detail_id>/delete/', shipping_views.delete_order_detail, name='shipping_delete_detail'),
    path('shipping/<int:order_id>/edit/', shipping_views.order_edit, name='shipping_edit_order'),
    path('shipping/<int:order_id>/details/', shipping_views.order_details, name='shipping_order_details'),

    path('shipping/load/customer/info/', shipping_views.load_customer_info, name='shipping_load_customer'),

]
