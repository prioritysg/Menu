from django.db import models

from app.models import Organization


class Item(models.Model):
    active = models.BooleanField(default=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item_code = models.CharField(max_length=48)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class ItemUom(models.Model):
    CASE = 1
    PACK_TYPE_CHOICES = (
        (CASE, 'Case'),
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    pack = models.IntegerField()
    pack_type = models.ForeignKey('ItemPack', on_delete=models.CASCADE)
    upc = models.CharField(max_length=16)
    sku = models.CharField(max_length=32)
    weight_eng = models.FloatField()
    length_eng = models.FloatField()
    width_eng = models.FloatField()
    height_eng = models.FloatField()
    weight_metric = models.FloatField()
    length_metric = models.FloatField()
    width_metric = models.FloatField()
    height_metric = models.FloatField()

    def __str__(self):
        return str(self.id)


class ItemPack(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title
