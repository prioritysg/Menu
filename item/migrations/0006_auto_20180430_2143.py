# Generated by Django 2.0 on 2018-04-30 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20180430_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemuom',
            name='sku',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='itemuom',
            name='upc',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
