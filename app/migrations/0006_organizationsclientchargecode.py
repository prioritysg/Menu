# Generated by Django 2.0 on 2018-04-02 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationsClientChargeCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_code', models.CharField(choices=[('rec-admin', 'REC-ADMIN'), ('rec-pallet', 'REC-PALLET'), ('rec-carton', 'REC-CARTON'), ('rec-unit', 'REC-UNIT'), ('rec-cft-carton', 'REC-CFT-CARTON'), ('rec-cft-unit', 'REC-CFT-UNIT'), ('rec-storage-cft-carton', 'REC-STORAGE-CFT-CARTON'), ('rec-storage-cft-unit', 'REC-STORAGE-CFT-UNIT'), ('ship-admin', 'SHIP-ADMIN'), ('ship-pallet', 'SHIP-PALLET'), ('ship-carton', 'SHIP-CARTON'), ('ship-unit', 'SHIP-UNIT'), ('ship-cft-carton', 'SHIP-CFT-CARTON'), ('ship-cft-unit', 'SHIP-CFT-UNIT'), ('storage-admin', 'STORAGE-ADMIN'), ('storage-pallet', 'STORAGE-PALLET'), ('storage-carton', 'STORAGE-CARTON'), ('storage-unit', 'STORAGE-UNIT')], max_length=16)),
                ('description', models.CharField(choices=[('receiving-by-pallet', 'RECEIVING BY PALLET'), ('receiving-by-carton', 'RECEIVING BY CARTON'), ('receiving-by-unit', 'RECEIVING BY UNIT'), ('receiving-by-cft-carton', 'RECEIVING BY CFT CARTON'), ('receiving-by-cft-unit', 'RECEIVING BY CFT UNIT'), ('receiving-storage-by-pallet', 'RECEIVING STORAGE BY PALLET'), ('receiving-storage-by-carton', 'RECEIVING STORAGE BY CARTON'), ('receiving-storage-by-unit', 'RECEIVING STORAGE BY UNIT'), ('receiving-storage-by-cft-carton', 'RECEIVING STORAGE BY CFT CARTON'), ('receiving-storage-by-cft-unit', 'RECEIVING STORAGE BY CFT UNIT'), ('shipping-administrative', 'SHIPPING ADMINISTRATIVE'), ('shipping-by-pallet', 'SHIPPING BY PALLET'), ('shipping-by-carton', 'SHIPPING BY CARTON'), ('shipping-by-unit', 'SHIPPING BY UNIT'), ('shipping-by-cft-carton', 'SHIPPING BY CFT CARTON'), ('shipping-by-cft-unit', 'SHIPPING BY CFT UNIT'), ('storage-administrative', 'STORAGE ADMINISTRATIVE'), ('storage-by-pallet', 'STORAGE BY PALLET'), ('storage-by-carton', 'STORAGE BY CARTON'), ('storage-by-unit', 'STORAGE BY UNIT'), ('storage-cft-carton', 'STORAGE BY_CFT_CARTON')], max_length=32)),
                ('rate_per', models.CharField(choices=[('pallet', 'pallet'), ('carton', 'carton'), ('unit', 'unit'), ('fixed', 'fixed')], max_length=16)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Organization')),
            ],
            options={
                'db_table': 'app_organizations_client_chargecodes',
            },
        ),
    ]
