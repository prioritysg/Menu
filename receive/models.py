from django.db import models

from app.models import Organization
from item.models import Item, ItemUom


class Order(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    order_no = models.IntegerField()
    ref_no = models.IntegerField()
    status = models.CharField(max_length=10)
    expected_arrival_date = models.DateField()
    actual_arrival_date = models.DateField(null=True, blank=True)
    receive_start_date = models.DateField(null=True, blank=True)
    receive_finish_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.order_no


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    line_number = models.IntegerField(default=1)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    itemuom = models.ForeignKey(ItemUom, on_delete=models.CASCADE)
    weight = models.FloatField(default=0.0)
    item_udf1 = models.CharField(max_length=32)
    item_udf2 = models.CharField(max_length=32)
    quantity_requested = models.IntegerField(default=1)
    quantity_received = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)
