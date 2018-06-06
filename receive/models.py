from django.db import models

from app.models import Organization
from item.models import Item, ItemUom


class Order(models.Model):
    OPEN = 'open'
    WIP = 'wip'
    HOLD = 'hold'
    RECEIVE = 'receive'
    CLOSED = 'closed'
    INVOICED = 'invoiced'
    CANCELLED = 'cancelled'

    STATUS_CHOICES = (
        (OPEN, 'Open'),
        (WIP, 'Wip'),
        (HOLD, 'Hold'),
        (RECEIVE, 'Receive'),
        (CLOSED, 'Closed'),
        (INVOICED, 'Invoiced'),
        (CANCELLED, 'Cancelled'),
    )
    ORDER = 'ORDER'
    SHIPPING = 'SHIPPING'
    ORDER_TYPE = (
        (ORDER, 'Order'),
        (SHIPPING, 'Shipping'),
    )

    order_type = models.CharField(max_length=20, choices=ORDER_TYPE, default=ORDER)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    order_no = models.IntegerField(unique=True)
    ref_no = models.CharField(max_length=50, default='')
    ponumber = models.CharField(max_length=32, default='')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=OPEN)
    expected_arrival_date = models.DateField()
    actual_arrival_date = models.DateField(null=True, blank=True)
    receive_start_date = models.DateField(null=True, blank=True)
    receive_finish_date = models.DateField(null=True, blank=True)
    container = models.CharField(max_length=50, default='')
    carrier = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='order_carrier', null=True,
                                blank=True)
    organization_customer = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True,
                                              related_name='order_customer_org')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.order_no)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    itemuom = models.ForeignKey(ItemUom, on_delete=models.CASCADE)
    line_number = models.IntegerField(default=1)
    weight = models.FloatField(default=0.0)
    item_udf1 = models.CharField(max_length=32, null=True, blank=True)
    item_udf2 = models.CharField(max_length=32, null=True, blank=True)
    quantity_requested = models.IntegerField(default=0)
    quantity_received = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
