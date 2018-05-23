from django import forms

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
        super(OrderDetailForm, self).__init__(*args, **kwargs)
