from django import forms

from app.models import Organization
from item.models import Item, ItemUom
from receive.models import OrderDetail, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)


class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        order_id = kwargs.pop('order_id')
        super(OrderDetailForm, self).__init__(*args, **kwargs)

        if order_id != -1:
            self.fields['order'].initial = Order.objects.filter(id=order_id).first()
            self.fields['order'].queryset = Order.objects.filter(id=order_id)
            self.fields['order'].widget = forms.HiddenInput()
            items = Item.objects.filter(
                organization=Order.objects.filter(id=order_id).first().organization)
            self.fields['item'].queryset = items
            self.fields['itemuom'].queryset = ItemUom.objects.filter(item__in=items)
        else:
            items = Item.objects.filter(organization__category=Organization.CLIENT)
            self.fields['item'].queryset = items
            self.fields['itemuom'].queryset = ItemUom.objects.filter(item__in=items)

        if self.instance and self.instance.pk:
            self.fields['order'].widget.attrs['readonly'] = True
            self.fields['item'].widget.attrs['readonly'] = True
            self.fields['itemuom'].widget.attrs['readonly'] = True


        #     self.fields['item'].widget = forms.HiddenInput()
            #
            # self.fields['item'].empty_label = None
            # self.fields['pack_type'].empty_label = None
