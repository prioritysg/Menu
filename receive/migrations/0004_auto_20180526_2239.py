# Generated by Django 2.0 on 2018-05-26 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receive', '0003_auto_20180523_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ref_no',
            field=models.CharField(default='', max_length=50),
        ),
    ]
