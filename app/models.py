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
