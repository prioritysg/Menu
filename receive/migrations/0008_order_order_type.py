# Generated by Django 2.0 on 2018-06-05 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receive', '0007_auto_20180605_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[('ORDER', 'Order'), ('SHIPPING', 'Shipping')], default='ORDER', max_length=20),
        ),
    ]
