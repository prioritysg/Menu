from django.db import models

from app.models import Organization


class Item(models.Model):
    active = models.BooleanField(default=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item_code = models.CharField(max_length=48)
    description = models.CharField(max_length=100)

    class Meta:
        unique_together = (("organization", "item_code"),)

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
    upc = models.CharField(max_length=16, null=True, blank=True)
    sku = models.CharField(max_length=32, null=True, blank=True)
    weight_eng = models.FloatField(default=0.0)
    length_eng = models.FloatField(default=0.0)
    width_eng = models.FloatField(default=0.0)
    height_eng = models.FloatField(default=0.0)
    weight_metric = models.FloatField(default=0.0)
    length_metric = models.FloatField(default=0.0)
    width_metric = models.FloatField(default=0.0)
    height_metric = models.FloatField(default=0.0)

    class Meta:
        unique_together = (("item", "pack", "pack_type"),)

    def __str__(self):
        return str('%s - %s' % (str(self.pack), str(self.pack_type)))


class ItemPack(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title
