# Generated by Django 2.0 on 2018-05-03 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_auto_20180430_2144'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='itemuom',
            unique_together={('item', 'pack', 'pack_type')},
        ),
    ]
