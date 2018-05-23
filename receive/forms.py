from django import forms

from app.models import Organization
from item.models import Item, ItemUom
from receive.models import OrderDetail, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailMForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = '__all__'
