# Generated by Django 2.0 on 2018-04-03 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_organizationsclientchargecode'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationsCarrierDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrier_type', models.CharField(choices=[('ltl', 'LTL'), ('parcel', 'Parcel')], max_length=15)),
                ('carrier_scac', models.CharField(max_length=8)),
                ('domestic_1am_active', models.BooleanField(default=True)),
                ('domestic_1am_scac', models.CharField(max_length=8)),
                ('domestic_1_active', models.BooleanField(default=True)),
                ('domestic_1_scac', models.CharField(max_length=8)),
                ('domestic_2am_active', models.BooleanField(default=True)),
                ('domestic_2am_scac', models.CharField(max_length=8)),
                ('domestic_2_active', models.BooleanField(default=True)),
                ('domestic_2_scac', models.CharField(max_length=8)),
                ('domestic_3_active', models.BooleanField(default=True)),
                ('domestic_3_scac', models.CharField(max_length=8)),
                ('domestic_ground_active', models.BooleanField(default=True)),
                ('domestic_ground_scac', models.CharField(max_length=8)),
                ('intl_1_active', models.BooleanField(default=True)),
                ('intl_1_scac', models.CharField(max_length=8)),
                ('intl_2_active', models.BooleanField(default=True)),
                ('intl_2_scac', models.CharField(max_length=8)),
                ('intl_3_active', models.BooleanField(default=True)),
                ('intl_3_scac', models.CharField(max_length=8)),
                ('intl_ground_active', models.BooleanField(default=True)),
                ('intl_ground_scac', models.CharField(max_length=8)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Organization')),
            ],
            options={
                'db_table': 'app_organizations_carrier_details',
            },
        ),
        migrations.AlterField(
            model_name='organizationsclientchargecode',
            name='rate_per',
            field=models.CharField(choices=[('pallet', 'Pallet'), ('carton', 'Carton'), ('unit', 'Unit'), ('fixed', 'Fixed')], max_length=16),
        ),
    ]
