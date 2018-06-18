from django import forms

from app.models import Organization
from item.models import Item, ItemUom
from receive.models import OrderDetail, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('ponumber', 'organization_customer', 'order_type',)

    def __init__(self, *args, **kwargs):
        order_id = kwargs.pop('order_id')
        super(OrderForm, self).__init__(*args, **kwargs)

        self.fields['expected_arrival_date'].label = "Expected Arrival Date"
        self.fields['actual_arrival_date'].label = "Actual Arrival Date"
        self.fields['receive_start_date'].label = "Receive Start Date"
        self.fields['receive_finish_date'].label = "Receive Finish Date"

        if order_id != -1:
            self.fields['organization'].initial = Organization.objects.filter(id=order_id).first()
            self.fields['organization'].widget = forms.HiddenInput()

        if self.instance and self.instance.pk:
            if self.instance.expected_arrival_date:
                self.fields['expected_arrival_date'].initial = self.instance.expected_arrival_date.strftime('%Y-%m-%d')
            if self.instance.actual_arrival_date:
                self.fields['actual_arrival_date'].initial = self.instance.actual_arrival_date.strftime('%Y-%m-%d')
            if self.instance.receive_start_date:
                self.fields['receive_start_date'].initial = self.instance.receive_start_date.strftime('%Y-%m-%d')
            if self.instance.receive_finish_date:
                self.fields['receive_finish_date'].initial = self.instance.receive_finish_date.strftime('%Y-%m-%d')
            if self.instance.cancel_date:
                self.fields['cancel_date'].initial = self.instance.cancel_date.strftime('%Y-%m-%d')

            self.fields['expected_arrival_date'].widget = forms.widgets.DateInput(attrs={'type': 'date',})
            self.fields['actual_arrival_date'].widget = forms.widgets.DateInput(attrs={'type': 'date',})
            self.fields['receive_start_date'].widget = forms.widgets.DateInput(attrs={'type': 'date',})
            self.fields['receive_finish_date'].widget = forms.widgets.DateInput(attrs={'type': 'date',})
            self.fields['cancel_date'].widget = forms.widgets.DateInput(attrs={'type': 'date',})

        else:
            self.fields['expected_arrival_date'].widget = forms.widgets.DateInput(attrs={'type': 'date',},
                                                                                  format=('%m/%d/%Y'))
            self.fields['actual_arrival_date'].widget = forms.widgets.DateInput(attrs={'type': 'date',},
                                                                                format=('%m/%d/%Y'))
            self.fields['receive_start_date'].widget = forms.widgets.DateInput(attrs={'type': 'date',},
                                                                               format=('%m/%d/%Y'))
            self.fields['receive_finish_date'].widget = forms.widgets.DateInput(attrs={'type': 'date',},
                                                                                format=('%m/%d/%Y'))
            self.fields['cancel_date'].widget = forms.widgets.DateInput(attrs={'type': 'date',},
                                                                        format=('%m/%d/%Y'))

        self.fields['carrier'].queryset = Organization.objects.filter(category=Organization.CARRIER)
        self.fields['organization'].queryset = Organization.objects.filter(category=Organization.CLIENT)


class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        order_id = kwargs.pop('order_id')
        super(OrderDetailForm, self).__init__(*args, **kwargs)

        self.fields['quantity_requested'].label = "Quantity Requested"
        self.fields['quantity_received'].label = "Quantity Shipped"

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
            self.fields['order'].widget = forms.HiddenInput()
            items = Item.objects.filter(organization=self.instance.order.organization)
            self.fields['item'].queryset = items
            self.fields['itemuom'].queryset = ItemUom.objects.filter(item__in=items)


class ShippingOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('receive_start_date', 'receive_finish_date', 'order_type', 'container')

    def __init__(self, *args, **kwargs):
        order_id = kwargs.pop('order_id')
        super(ShippingOrderForm, self).__init__(*args, **kwargs)

        self.fields['expected_arrival_date'].label = "Requested Ship Date"
        self.fields['actual_arrival_date'].label = "Actual Ship Date"
        self.fields['organization_customer'].label = "Customer"

        if order_id != -1:
            self.fields['organization'].initial = Organization.objects.filter(id=order_id).first()
            self.fields['organization'].widget = forms.HiddenInput()

        if self.instance and self.instance.pk:
            if self.instance.expected_arrival_date:
                self.fields['expected_arrival_date'].initial = self.instance.expected_arrival_date.strftime('%Y-%m-%d')
            if self.instance.actual_arrival_date:
                self.fields['actual_arrival_date'].initial = self.instance.actual_arrival_date.strftime('%Y-%m-%d')
            if self.instance.cancel_date:
                self.fields['cancel_date'].initial = self.instance.cancel_date.strftime('%Y-%m-%d')

            self.fields['expected_arrival_date'].widget = forms.widgets.DateInput(attrs={'type': 'date',})
            self.fields['cancel_date'].widget = forms.widgets.DateInput(attrs={'type': 'date',})
            self.fields['actual_arrival_date'].widget = forms.widgets.DateInput(attrs={'type': 'date',})

        else:
            self.fields['expected_arrival_date'].widget = forms.widgets.DateInput(attrs={'type': 'date',},
                                                                                  format=('%m/%d/%Y'))
            self.fields['actual_arrival_date'].widget = forms.widgets.DateInput(attrs={'type': 'date',},
                                                                                format=('%m/%d/%Y'))
            self.fields['cancel_date'].widget = forms.widgets.DateInput(attrs={'type': 'date',},
                                                                        format=('%m/%d/%Y'))

        self.fields['carrier'].queryset = Organization.objects.filter(category=Organization.CARRIER)
        self.fields['organization_customer'].queryset = Organization.objects.filter(category=Organization.CUSTOMER)
        self.fields['organization'].queryset = Organization.objects.filter(category=Organization.CLIENT)
