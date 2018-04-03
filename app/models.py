from django.contrib.auth.models import User
from django.db import models


class UserGroup(models.Model):
    ADMIN = 'admin'
    MANAGER = 'manager'
    ASSISTANT = 'assistant'
    REGULAR = 'regular'
    CLIENT = 'client'

    USER_TYPES = (
        (ADMIN, 'Admin User'),
        (MANAGER, 'Manager User'),
        (ASSISTANT, 'Assistant User'),
        (REGULAR, 'Regular User'),
        (CLIENT, 'Client User'),

    )

    users = models.ManyToManyField(User)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default=REGULAR)

    def __str__(self):
        return self.user_type

    class Meta:
        db_table = 'app_user_group'


class GroupAccess(models.Model):
    NO_ACCESS = '0'
    READ = 'R'
    READ_WRITE = 'RW'
    ACCESSES = (
        (NO_ACCESS, 'No Access'),
        (READ, 'Read'),
        (READ_WRITE, 'Read Write'),
    )

    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE, db_column='app_user_group_link')
    receiving = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)
    shipping = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)
    mobile = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)
    inventory = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)
    items = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)
    reports = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)
    organization = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)
    security = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)
    client = models.CharField(max_length=5, choices=ACCESSES, default=NO_ACCESS)

    def __str__(self):
        return self.user_group.user_type

    class Meta:
        db_table = 'app_user_group_access'


class Organization(models.Model):
    CLIENT = 1
    CUSTOMER = 2
    CARRIER = 3
    CATEGORIES_CHOICES = (
        (CLIENT, 'Client'),
        (CUSTOMER, 'Customer'),
        (CARRIER, 'Carrier'),
    )

    org_id = models.CharField(max_length=16)
    active = models.BooleanField(default=False)
    category = models.PositiveSmallIntegerField(choices=CATEGORIES_CHOICES)
    description = models.TextField()
    mt_address1 = models.CharField(max_length=64)
    mt_address2 = models.CharField(max_length=64, null=True, blank=True)
    mt_address3 = models.CharField(max_length=64, null=True, blank=True)
    mt_city = models.CharField(max_length=64)
    mt_state = models.CharField(max_length=16)
    mt_zip = models.CharField(max_length=16)
    mt_country = models.CharField(max_length=64)
    st_address1 = models.CharField(max_length=64)
    st_address2 = models.CharField(max_length=64, null=True, blank=True)
    st_address3 = models.CharField(max_length=64, null=True, blank=True)
    st_city = models.CharField(max_length=64)
    st_state = models.CharField(max_length=16)
    st_zip = models.CharField(max_length=16)
    st_country = models.CharField(max_length=64)

    def __str__(self):
        return self.org_id


class OrganizationsClientChargeCode(models.Model):
    PALLET = 'pallet'
    CARTON = 'carton'
    UNIT = 'unit'
    FIXED = 'fixed'

    RATE_PER_CHOICES = (
        (PALLET, 'Pallet'),
        (CARTON, 'Carton'),
        (UNIT, 'Unit'),
        (FIXED, 'Fixed'),
    )
    REC_ADMIN = 'rec-admin'
    REC_PALLET = 'rec-pallet'
    REC_CARTON = 'rec-carton'
    REC_UNIT = 'rec-unit'
    REC_CFT_CARTON = 'rec-cft-carton'
    REC_CFT_UNIT = 'rec-cft-unit'
    REC_STORAGE_CFT_CARTON = 'rec-storage-cft-carton'
    REC_STORAGE_CFT_UNIT = 'rec-storage-cft-unit'
    SHIP_ADMIN = 'ship-admin'
    SHIP_PALLET = 'ship-pallet'
    SHIP_CARTON = 'ship-carton'
    SHIP_UNIT = 'ship-unit'
    SHIP_CFT_CARTON = 'ship-cft-carton'
    SHIP_CFT_UNIT = 'ship-cft-unit'
    STORAGE_ADMIN = 'storage-admin'
    STORAGE_PALLET = 'storage-pallet'
    STORAGE_CARTON = 'storage-carton'
    STORAGE_UNIT = 'storage-unit'
    STORAGE_CFT_CARTON = 'storage-cft-carton'

    CHARGE_CODE_CHOICES = (
        (REC_ADMIN, 'REC-ADMIN'),
        (REC_PALLET, 'REC-PALLET'),
        (REC_CARTON, 'REC-CARTON'),
        (REC_UNIT, 'REC-UNIT'),
        (REC_CFT_CARTON, 'REC-CFT-CARTON'),
        (REC_CFT_UNIT, 'REC-CFT-UNIT'),
        (REC_STORAGE_CFT_CARTON, 'REC-STORAGE-CFT-CARTON'),
        (REC_STORAGE_CFT_UNIT, 'REC-STORAGE-CFT-UNIT'),
        (SHIP_ADMIN, 'SHIP-ADMIN'),
        (SHIP_PALLET, 'SHIP-PALLET'),
        (SHIP_CARTON, 'SHIP-CARTON'),
        (SHIP_UNIT, 'SHIP-UNIT'),
        (SHIP_CFT_CARTON, 'SHIP-CFT-CARTON'),
        (SHIP_CFT_UNIT, 'SHIP-CFT-UNIT'),
        (STORAGE_ADMIN, 'STORAGE-ADMIN'),
        (STORAGE_PALLET, 'STORAGE-PALLET'),
        (STORAGE_CARTON, 'STORAGE-CARTON'),
        (STORAGE_UNIT, 'STORAGE-UNIT'),
    )

    RECEIVING_BY_PALLET = 'receiving-by-pallet'
    RECEIVING_BY_CARTON = 'receiving-by-carton'
    RECEIVING_BY_UNIT = 'receiving-by-unit'
    RECEIVING_BY_CFT_CARTON = 'receiving-by-cft-carton'
    RECEIVING_BY_CFT_UNIT = 'receiving-by-cft-unit'
    RECEIVING_STORAGE_BY_PALLET = 'receiving-storage-by-pallet'
    RECEIVING_STORAGE_BY_CARTON = 'receiving-storage-by-carton'
    RECEIVING_STORAGE_BY_UNIT = 'receiving-storage-by-unit'
    RECEIVING_STORAGE_BY_CFT_CARTON = 'receiving-storage-by-cft-carton'
    RECEIVING_STORAGE_BY_CFT_UNIT = 'receiving-storage-by-cft-unit'
    SHIPPING_ADMINISTRATIVE = 'shipping-administrative'
    SHIPPING_BY_PALLET = 'shipping-by-pallet'
    SHIPPING_BY_CARTON = 'shipping-by-carton'
    SHIPPING_BY_UNIT = 'shipping-by-unit'
    SHIPPING_BY_CFT_CARTON = 'shipping-by-cft-carton'
    SHIPPING_BY_CFT_UNIT = 'shipping-by-cft-unit'
    STORAGE_ADMINISTRATIVE = 'storage-administrative'
    STORAGE_BY_PALLET = 'storage-by-pallet'
    STORAGE_BY_CARTON = 'storage-by-carton'
    STORAGE_BY_UNIT = 'storage-by-unit'
    STORAGE_BY_CFT_CARTON = 'storage-cft-carton'

    DESCRIPTION_CHOICES = (
        (RECEIVING_BY_PALLET, 'RECEIVING BY PALLET'),
        (RECEIVING_BY_CARTON, 'RECEIVING BY CARTON'),
        (RECEIVING_BY_UNIT, 'RECEIVING BY UNIT'),
        (RECEIVING_BY_CFT_CARTON, 'RECEIVING BY CFT CARTON'),
        (RECEIVING_BY_CFT_UNIT, 'RECEIVING BY CFT UNIT'),
        (RECEIVING_STORAGE_BY_PALLET, 'RECEIVING STORAGE BY PALLET'),
        (RECEIVING_STORAGE_BY_CARTON, 'RECEIVING STORAGE BY CARTON'),
        (RECEIVING_STORAGE_BY_UNIT, 'RECEIVING STORAGE BY UNIT'),
        (RECEIVING_STORAGE_BY_CFT_CARTON, 'RECEIVING STORAGE BY CFT CARTON'),
        (RECEIVING_STORAGE_BY_CFT_UNIT, 'RECEIVING STORAGE BY CFT UNIT'),
        (SHIPPING_ADMINISTRATIVE, 'SHIPPING ADMINISTRATIVE'),
        (SHIPPING_BY_PALLET, 'SHIPPING BY PALLET'),
        (SHIPPING_BY_CARTON, 'SHIPPING BY CARTON'),
        (SHIPPING_BY_UNIT, 'SHIPPING BY UNIT'),
        (SHIPPING_BY_CFT_CARTON, 'SHIPPING BY CFT CARTON'),
        (SHIPPING_BY_CFT_UNIT, 'SHIPPING BY CFT UNIT'),
        (STORAGE_ADMINISTRATIVE, 'STORAGE ADMINISTRATIVE'),
        (STORAGE_BY_PALLET, 'STORAGE BY PALLET'),
        (STORAGE_BY_CARTON, 'STORAGE BY CARTON'),
        (STORAGE_BY_UNIT, 'STORAGE BY UNIT'),
        (STORAGE_BY_CFT_CARTON, 'STORAGE BY_CFT_CARTON')
    )

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, )
    charge_code = models.CharField(max_length=16, choices=CHARGE_CODE_CHOICES)
    description = models.CharField(max_length=32, choices=DESCRIPTION_CHOICES)
    rate_per = models.CharField(max_length=16, choices=RATE_PER_CHOICES)
    rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.charge_code

    class Meta:
        db_table = 'app_organizations_client_chargecodes'


class OrganizationsCarrierDetail(models.Model):
    LTL = 'ltl'
    PARCEL = 'parcel'

    CARRIER_TYPE_CHOICES = ((LTL, 'LTL'), (PARCEL, 'Parcel'))

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, )
    carrier_type = models.CharField(max_length=15, choices=CARRIER_TYPE_CHOICES)
    carrier_scac = models.CharField(max_length=8)
    domestic_1am_active = models.BooleanField(default=True)
    domestic_1am_scac = models.CharField(max_length=8)
    domestic_1_active = models.BooleanField(default=True)
    domestic_1_scac = models.CharField(max_length=8)
    domestic_2am_active = models.BooleanField(default=True)
    domestic_2am_scac = models.CharField(max_length=8)
    domestic_2_active = models.BooleanField(default=True)
    domestic_2_scac = models.CharField(max_length=8)
    domestic_3_active = models.BooleanField(default=True)
    domestic_3_scac = models.CharField(max_length=8)
    domestic_ground_active = models.BooleanField(default=True)
    domestic_ground_scac = models.CharField(max_length=8)
    intl_1_active = models.BooleanField(default=True)
    intl_1_scac = models.CharField(max_length=8)
    intl_2_active = models.BooleanField(default=True)
    intl_2_scac = models.CharField(max_length=8)
    intl_3_active = models.BooleanField(default=True)
    intl_3_scac = models.CharField(max_length=8)
    intl_ground_active = models.BooleanField(default=True)
    intl_ground_scac = models.CharField(max_length=8)

    def __str__(self):
        return self.carrier_type

    class Meta:
        db_table = 'app_organizations_carrier_details'
