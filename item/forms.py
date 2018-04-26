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
        else:
            self.fields['organization'].queryset = Organization.objects.filter(category=Organization.CLIENT)


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
        else:
            self.fields['item'].queryset = Item.objects.all()
