# Generated by Django 2.0 on 2018-04-30 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_auto_20180430_2143'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='itemuom',
            unique_together={('pack', 'pack_type')},
        ),
    ]
