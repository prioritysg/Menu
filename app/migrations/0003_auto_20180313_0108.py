# Generated by Django 2.0 on 2018-03-13 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180309_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupaccess',
            name='client',
            field=models.CharField(choices=[('0', 'No Access'), ('R', 'Read'), ('RW', 'Read Write')], default='0', max_length=5),
        ),
        migrations.AlterField(
            model_name='groupaccess',
            name='inventory',
            field=models.CharField(choices=[('0', 'No Access'), ('R', 'Read'), ('RW', 'Read Write')], default='0', max_length=5),
        ),
        migrations.AlterField(
            model_name='groupaccess',
            name='items',
            field=models.CharField(choices=[('0', 'No Access'), ('R', 'Read'), ('RW', 'Read Write')], default='0', max_length=5),
        ),
        migrations.AlterField(
            model_name='groupaccess',
            name='mobile',
            field=models.CharField(choices=[('0', 'No Access'), ('R', 'Read'), ('RW', 'Read Write')], default='0', max_length=5),
        ),
        migrations.AlterField(
            model_name='groupaccess',
            name='organization',
            field=models.CharField(choices=[('0', 'No Access'), ('R', 'Read'), ('RW', 'Read Write')], default='0', max_length=5),
        ),
        migrations.AlterField(
            model_name='groupaccess',
            name='receiving',
            field=models.CharField(choices=[('0', 'No Access'), ('R', 'Read'), ('RW', 'Read Write')], default='0', max_length=5),
        ),
        migrations.AlterField(
            model_name='groupaccess',
            name='reports',
            field=models.CharField(choices=[('0', 'No Access'), ('R', 'Read'), ('RW', 'Read Write')], default='0', max_length=5),
        ),
        migrations.AlterField(
            model_name='groupaccess',
            name='security',
            field=models.CharField(choices=[('0', 'No Access'), ('R', 'Read'), ('RW', 'Read Write')], default='0', max_length=5),
        ),
        migrations.AlterField(
            model_name='groupaccess',
            name='shipping',
            field=models.CharField(choices=[('0', 'No Access'), ('R', 'Read'), ('RW', 'Read Write')], default='0', max_length=5),
        ),
    ]