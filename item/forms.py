from django import forms

from app.models import Organization
from item.models import Item, ItemUom


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('organization', 'item_code', 'description', 'active')

    def __init__(self, *args, **kwargs):
        org_id = kwargs.pop('org_id')
        super(ItemForm, self).__init__(*args, **kwargs)
        if org_id != -1:
            self.fields['organization'].initial = Organization.objects.filter(id=org_id).first()
            self.fields['organization'].queryset = Organization.objects.filter(id=org_id)
            self.fields['organization'].widget = forms.HiddenInput()
        else:
            self.fields['organization'].queryset = Organization.objects.filter(category=Organization.CLIENT).order_by(
                'org_id')

        self.fields['organization'].empty_label = None


class ItemUOMForm(forms.ModelForm):
    weight_eng = forms.FloatField(required=False, initial=0.0)
    length_eng = forms.FloatField(required=False, initial=0.0)
    width_eng = forms.FloatField(required=False, initial=0.0)
    height_eng = forms.FloatField(required=False, initial=0.0)
    weight_metric = forms.FloatField(required=False, initial=0.0)
    length_metric = forms.FloatField(required=False, initial=0.0)
    width_metric = forms.FloatField(required=False, initial=0.0)
    height_metric = forms.FloatField(required=False, initial=0.0)

    class Meta:
        model = ItemUom
        fields = ('item', 'pack_type', 'pack', 'upc', 'sku', 'weight_eng', 'length_eng', 'width_eng', 'height_eng',
                  'weight_metric', 'length_metric', 'width_metric', 'height_metric')

    def __init__(self, *args, **kwargs):
        item_id = kwargs.pop('item_id')
        super(ItemUOMForm, self).__init__(*args, **kwargs)
        if item_id != -1:
            self.fields['item'].initial = Item.objects.filter(id=item_id).first()
            self.fields['item'].queryset = Item.objects.filter(id=item_id)
            self.fields['item'].widget = forms.HiddenInput()
        else:
            self.fields['item'].queryset = Item.objects.all()

        if self.instance and self.instance.pk:
            self.fields['item'].widget.attrs['readonly'] = True
            self.fields['pack'].widget.attrs['readonly'] = True
            self.fields['item'].widget = forms.HiddenInput()

        self.fields['item'].empty_label = None
        self.fields['pack_type'].empty_label = None
