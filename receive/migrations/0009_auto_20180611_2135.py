# Generated by Django 2.0 on 2018-06-11 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receive', '0008_order_order_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='container',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
