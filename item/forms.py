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
            self.fields['organization'].queryset = Organization.objects.filter(category=Organization.CLIENT)

        self.fields['organization'].empty_label = None


class ItemUOMForm(forms.ModelForm):
    class Meta:
        model = ItemUom
        fields = '__all__'

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
