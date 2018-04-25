from django import forms

from item.models import Item, ItemUom


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('organization', 'item_code', 'description', 'active')


class ItemUOMForm(forms.ModelForm):
    class Meta:
        model = ItemUom
        fields = '__all__'
