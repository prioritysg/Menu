# Generated by Django 2.0 on 2018-04-30 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20180427_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Organization', unique=True),
        ),
    ]
